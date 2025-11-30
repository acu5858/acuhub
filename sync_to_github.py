#!/usr/bin/env python3
"""
Auto-sync Replit changes to GitHub
Çalıştır: python sync_to_github.py
"""

import os
import time
import subprocess
from pathlib import Path

REPO_PATH = "/home/runner/workspace"
os.chdir(REPO_PATH)

print("🔄 Replit → GitHub Auto-Sync başladı...")
print("(Ctrl+C ile durdurabilirsin)\n")

# İlk commit varsa push et
try:
    subprocess.run(["git", "push", "origin", "main"], check=True, capture_output=True)
    print("✅ İlk push başarılı!")
except:
    print("⚠️ İlk push hatası (normal)")

# Her 30 saniyede bir kontrol et
last_hash = None
while True:
    try:
        # Değişiklikleri kontrol et
        result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        current_hash = hash(result.stdout)
        
        if current_hash != last_hash and result.stdout.strip():
            print(f"\n📝 Değişiklik algılandı:")
            print(result.stdout)
            
            # Commit ve push
            subprocess.run(["git", "add", "-A"], check=True, capture_output=True)
            subprocess.run(
                ["git", "commit", "-m", f"Auto-sync: {time.strftime('%Y-%m-%d %H:%M:%S')}"],
                check=True,
                capture_output=True
            )
            result = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
            print("✅ GitHub'a pushlandı!")
            last_hash = current_hash
        
        time.sleep(30)  # 30 saniye bekle
        
    except KeyboardInterrupt:
        print("\n\n👋 Sync durduruldu.")
        break
    except Exception as e:
        print(f"❌ Hata: {e}")
        time.sleep(60)
