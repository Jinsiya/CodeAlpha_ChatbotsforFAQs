# FAQ Chatbot Setup Script for PowerShell
Write-Host "🚀 Setting up FAQ Chatbot..." -ForegroundColor Cyan

# Check if Python is installed
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Python is not installed. Please install Python 3.8 or higher." -ForegroundColor Red
    exit 1
}