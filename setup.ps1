# Day 0 环境初始化（PowerShell）

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

Write-Host ">>> [1/4] 检查 conda..." -ForegroundColor Cyan
conda --version

Write-Host ">>> [2/4] 创建环境 job-hunt (python 3.11)..." -ForegroundColor Cyan
conda create -n job-hunt python=3.11 -y 2>$null
Write-Host "    请在新终端执行: conda activate job-hunt" -ForegroundColor Yellow

Write-Host ">>> [3/4] 安装依赖（需先 activate job-hunt）..." -ForegroundColor Cyan
Write-Host "    pip install -r requirements.txt" -ForegroundColor Yellow

Write-Host ">>> [4/4] 配置密钥..." -ForegroundColor Cyan
if (-not (Test-Path ".env")) {
    Copy-Item ".env.example" ".env"
    Write-Host "    已创建 .env，请编辑填入 API Key" -ForegroundColor Green
} else {
    Write-Host "    .env 已存在，跳过" -ForegroundColor Gray
}

Write-Host ""
Write-Host "下一步:" -ForegroundColor Green
Write-Host "  1. conda activate job-hunt"
Write-Host "  2. pip install -r requirements.txt"
Write-Host "  3. 编辑 .env 填入 DEEPSEEK_API_KEY"
Write-Host "  4. python scripts/hello_llm.py"
