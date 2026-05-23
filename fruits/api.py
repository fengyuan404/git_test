"""🍉 Fruit Catalog REST API — FastAPI 驱动的营养数据微服务。"""

from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, Response
from . import data
from . import analytics
from . import dashboard

app = FastAPI(
    title="🍉 Fruit Catalog API",
    description="一个基于真实营养数据的水果目录 REST API",
    version="2.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
def root():
    return dashboard.DASHBOARD_HTML


@app.get("/api")
def api_root():
    return {
        "service": "Fruit Catalog API",
        "version": "2.0.0",
        "docs": "/docs",
        "dashboard": "/",
        "endpoints": {
            "所有水果": "/fruits",
            "单个水果": "/fruits/{name}",
            "搜索": "/fruits/search?q=莓",
            "季节筛选": "/fruits/season/夏季",
            "Top排行": "/fruits/top/kcal?n=3",
            "统计概览": "/fruits/stats",
            "SVG图表": "/chart/kcal",
        }
    }


@app.get("/fruits")
def get_all():
    items = data.get_all()
    return {"count": len(items), "fruits": items}


@app.get("/fruits/search")
def search_fruits(q: str = Query(..., description="搜索关键词")):
    result = data.search(q)
    return {"query": q, "count": len(result), "results": result}


@app.get("/fruits/stats")
def get_stats():
    return data.stats()


@app.get("/fruits/season/{season}")
def by_season(season: str):
    result = data.filter_by_season(season)
    return {"season": season, "count": len(result), "fruits": result}


@app.get("/fruits/top/{field}")
def top_n(
    field: str,
    n: int = Query(5, ge=1, le=20),
):
    valid_fields = ["kcal", "carbs", "protein", "fat", "fiber", "vitamin_c"]
    if field not in valid_fields:
        raise HTTPException(status_code=400, detail=f"无效字段，可选: {valid_fields}")
    result = data.top_by(field, n)
    return {"field": field, "count": len(result), "ranking": result}


@app.get("/fruits/{name}")
def get_one(name: str):
    fruit = data.get(name)
    if not fruit:
        raise HTTPException(status_code=404, detail=f"未找到水果「{name}」")
    return {"name": name, "nutrition": fruit}


@app.get("/chart/{field}")
def chart(field: str):
    """返回 SVG 营养对比柱状图，可直接在浏览器中查看"""
    valid_fields = ["kcal", "carbs", "protein", "fat", "fiber", "vitamin_c"]
    if field not in valid_fields:
        raise HTTPException(status_code=400, detail=f"无效字段，可选: {valid_fields}")
    svg = analytics.generate_chart(field)
    return Response(content=svg, media_type="image/svg+xml")
