"""🍉 Web Dashboard — 水果营养数据看板。"""

DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🍉 Fruit Catalog — 数据看板</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Microsoft YaHei', sans-serif; background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); color: #e0e0e0; min-height: 100vh; }
.header { text-align: center; padding: 40px 20px 20px; }
.header h1 { font-size: 2.5rem; background: linear-gradient(90deg, #f7971e, #ffd200); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.header p { color: #888; margin-top: 8px; }
.container { max-width: 1200px; margin: 0 auto; padding: 0 20px 40px; }
.stats-row { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 16px; margin-bottom: 30px; }
.stat-card { background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 20px; text-align: center; backdrop-filter: blur(10px); }
.stat-card .value { font-size: 2rem; font-weight: 700; background: linear-gradient(90deg, #f7971e, #ffd200); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.stat-card .label { color: #888; font-size: 0.85rem; margin-top: 4px; }
.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px; }
@media (max-width: 768px) { .grid-2 { grid-template-columns: 1fr; } }
.card { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 24px; backdrop-filter: blur(10px); }
.card h3 { font-size: 1.1rem; margin-bottom: 16px; color: #ffd200; }
.chart-wrap { position: relative; height: 280px; }
.chart-wrap canvas { width: 100% !important; }
.table-wrap { overflow-x: auto; }
table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
th, td { padding: 12px 16px; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.06); }
th { color: #ffd200; font-weight: 600; }
tbody tr:hover { background: rgba(255,255,255,0.04); }
.search-box { margin-bottom: 20px; display: flex; gap: 10px; }
.search-box input { flex: 1; padding: 10px 16px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.15); background: rgba(255,255,255,0.06); color: #e0e0e0; font-size: 0.95rem; outline: none; }
.search-box input:focus { border-color: #ffd200; }
.search-box button { padding: 10px 20px; border-radius: 8px; border: none; background: linear-gradient(135deg, #f7971e, #ffd200); color: #1a1a2e; font-weight: 600; cursor: pointer; }
.badge { display: inline-block; padding: 2px 10px; border-radius: 12px; font-size: 0.75rem; background: rgba(255,210,0,0.15); color: #ffd200; }
.api-link { text-align: center; margin-top: 10px; }
.api-link a { color: #888; text-decoration: none; font-size: 0.85rem; }
.api-link a:hover { color: #ffd200; }
</style>
</head>
<body>
<div class="header">
  <h1>🍉 Fruit Catalog</h1>
  <p>水果营养数据看板 &middot; 实时数据 &middot; 交互式图表</p>
</div>
<div class="container">
  <div class="stats-row" id="stats-row"></div>

  <div class="search-box">
    <input type="text" id="search-input" placeholder="🔍 搜索水果..." oninput="filterTable()">
    <button onclick="filterTable()">搜索</button>
  </div>

  <div class="grid-2">
    <div class="card">
      <h3>📊 营养指标对比</h3>
      <div class="chart-wrap"><canvas id="radarChart"></canvas></div>
    </div>
    <div class="card">
      <h3>🔥 热量排名</h3>
      <div class="chart-wrap"><canvas id="kcalChart"></canvas></div>
    </div>
  </div>

  <div class="card" style="margin-bottom:20px;">
    <h3>🥗 维生素C 含量对比</h3>
    <div class="chart-wrap"><canvas id="vitaminChart"></canvas></div>
  </div>

  <div class="card">
    <h3>📋 完整数据表</h3>
    <div class="table-wrap">
      <table id="fruit-table">
        <thead>
          <tr>
            <th>水果</th><th>热量<br>(kcal)</th><th>碳水<br>(g)</th><th>蛋白质<br>(g)</th>
            <th>脂肪<br>(g)</th><th>纤维<br>(g)</th><th>维C<br>(mg)</th><th>季节</th>
          </tr>
        </thead>
        <tbody></tbody>
      </table>
    </div>
  </div>

  <div class="api-link">
    <a href="/docs" target="_blank">📡 API 文档 (Swagger) →</a>
  </div>
</div>

<script>
const COLORS = ['#FF6384','#36A2EB','#FFCE56','#4BC0C0','#9966FF','#FF9F40','#C9CBCF','#7BC8A4','#E8A87C'];
let allData = {};

fetch('/fruits')
  .then(r => r.json())
  .then(d => {
    allData = d.fruits;
    renderStats(d.fruits, d.count);
    renderTable(d.fruits);
    renderRadar(d.fruits);
    renderKcalChart(d.fruits);
    renderVitaminChart(d.fruits);
  });

function renderStats(fruits, count) {
  const vals = Object.values(fruits);
  const avgKcal = (vals.reduce((s,v) => s+v.kcal, 0) / count).toFixed(0);
  const maxVC = Math.max(...vals.map(v => v.vitamin_c));
  const topVC = Object.entries(fruits).find(([k,v]) => v.vitamin_c === maxVC);
  document.getElementById('stats-row').innerHTML = `
    <div class="stat-card"><div class="value">${count}</div><div class="label">收录水果</div></div>
    <div class="stat-card"><div class="value">${avgKcal}</div><div class="label">平均热量 (kcal)</div></div>
    <div class="stat-card"><div class="value">${maxVC}mg</div><div class="label">最高维C — ${topVC[0]}</div></div>
    <div class="stat-card"><div class="value">∞</div><div class="label">REST API 端点</div></div>
  `;
}

function renderTable(fruits) {
  const tbody = document.querySelector('#fruit-table tbody');
  tbody.innerHTML = Object.entries(fruits).map(([name, d], i) => `
    <tr>
      <td><strong>${name}</strong></td>
      <td>${d.kcal}</td><td>${d.carbs}</td><td>${d.protein}</td>
      <td>${d.fat}</td><td>${d.fiber}</td><td>${d.vitamin_c}</td>
      <td><span class="badge">${d.season}</span></td>
    </tr>
  `).join('');
}

function filterTable() {
  const q = document.getElementById('search-input').value;
  const rows = document.querySelectorAll('#fruit-table tbody tr');
  rows.forEach(row => {
    row.style.display = row.textContent.includes(q) ? '' : 'none';
  });
}

function renderRadar(fruits) {
  const names = Object.keys(fruits);
  new Chart(document.getElementById('radarChart'), {
    type: 'radar',
    data: {
      labels: names,
      datasets: [
        { label: '热量', data: names.map(n => fruits[n].kcal), borderColor: '#FF6384', backgroundColor: 'rgba(255,99,132,0.1)' },
        { label: '碳水', data: names.map(n => fruits[n].carbs), borderColor: '#36A2EB', backgroundColor: 'rgba(54,162,235,0.1)' },
        { label: '纤维', data: names.map(n => fruits[n].fiber*10), borderColor: '#4BC0C0', backgroundColor: 'rgba(75,192,192,0.1)' },
      ]
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      scales: { r: { ticks: { color: '#888', backdropColor: 'transparent' }, grid: { color: 'rgba(255,255,255,0.08)' }, pointLabels: { color: '#ccc' } } },
      plugins: { legend: { labels: { color: '#ccc' } } }
    }
  });
}

function renderKcalChart(fruits) {
  const sorted = Object.entries(fruits).sort((a,b) => b[1].kcal - a[1].kcal);
  new Chart(document.getElementById('kcalChart'), {
    type: 'bar',
    data: {
      labels: sorted.map(([n]) => n),
      datasets: [{
        label: '热量 (kcal/100g)',
        data: sorted.map(([,d]) => d.kcal),
        backgroundColor: sorted.map((_,i) => COLORS[i % COLORS.length]),
        borderRadius: 6,
      }]
    },
    options: {
      responsive: true, maintainAspectRatio: false, indexAxis: 'y',
      scales: {
        x: { ticks: { color: '#888' }, grid: { color: 'rgba(255,255,255,0.06)' } },
        y: { ticks: { color: '#ccc' }, grid: { display: false } }
      },
      plugins: { legend: { display: false } }
    }
  });
}

function renderVitaminChart(fruits) {
  const sorted = Object.entries(fruits).sort((a,b) => b[1].vitamin_c - a[1].vitamin_c);
  new Chart(document.getElementById('vitaminChart'), {
    type: 'bar',
    data: {
      labels: sorted.map(([n]) => n),
      datasets: [{
        label: '维生素C (mg/100g)',
        data: sorted.map(([,d]) => d.vitamin_c),
        backgroundColor: sorted.map((_,i) => COLORS[i % COLORS.length]),
        borderRadius: 6,
      }]
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      scales: {
        x: { ticks: { color: '#888' }, grid: { color: 'rgba(255,255,255,0.06)' } },
        y: { ticks: { color: '#ccc', callback: v => v + ' mg' }, grid: { color: 'rgba(255,255,255,0.06)' } }
      },
      plugins: { legend: { display: true, labels: { color: '#ccc' } } }
    }
  });
}
</script>
</body>
</html>"""
