echo "==== Initialisation de ArcanApp MetaNiveaux ===="

# 1. Clonage et Intégration des Technologies Externes
echo "[1] Intégration Prophet (ChronoEcho+)"
git clone https://github.com/facebook/prophet.git --depth=1
cp -r prophet/python/prophet arcanapp/meta_modules/time_warper/
rm -rf prophet

echo "[2] Installation des bibliothèques nécessaires"
pip install -r requirements.txt

echo "[3] Lancement du dashboard ShadowOdds Live"
streamlit run app/core/realtime_dashboard.py

echo "==== ArcanApp initialisé avec succès ===="
