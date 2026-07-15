@echo off
cd /d C:\Users\asusp\OneDrive\Desktop\X2

git config user.email "msem7143@gmail.com"
git config user.name "msem7143-gif"

git add --all
git commit -m "Auto update HWIDS_PAGE from bot"
git push origin main --force

echo Done.