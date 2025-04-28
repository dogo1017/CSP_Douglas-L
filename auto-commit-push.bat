@echo off
cd "C:\Users\Douglas.london\Documents\CSP_Douglas-L"  :: Replace with the path to your project folder
git add .
git commit -m "Automated commit at %date% %time%"
git push origin main          :: Replace `main` with your branch name
