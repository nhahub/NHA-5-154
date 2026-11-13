WanderClimate: Free Render Deployment
====================================

1. Extract the deployment ZIP into the ROOT of the NHA-5-154 repository
   (the folder containing index.html and api.py).
2. From PowerShell in that folder:
      python apply_deployment_patch.py
      python -m pip install -r requirements-deploy.txt
      python -m uvicorn web_server:app --host 127.0.0.1 --port 8000
   Open http://127.0.0.1:8000/ and http://127.0.0.1:8000/health to test.
3. Commit and push the files to GitHub main, after reviewing git diff.
4. On https://dashboard.render.com choose New > Web Service.
5. Connect GitHub repository nhahub/NHA-5-154 (grant Render access if needed).
6. Branch: main; Language: Python; plan: Free.
   Build Command: pip install -r requirements-deploy.txt
   Start Command: uvicorn web_server:app --host 0.0.0.0 --port $PORT
   Health Check Path: /health
   Environment: PYTHON_VERSION = 3.11.11
7. Deploy. Open the HTTPS .onrender.com link Render provides.

Render's free instance has 512MB RAM and sleeps after 15 minutes idle.
If deployment fails due to memory or large data processing, check logs and
consider slimming the CSVs or hosting the API elsewhere.
Keep sensitive files such as .env and secrets.toml out of Git.
