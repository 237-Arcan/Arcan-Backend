from fastapi import FastAPI, HTTPException
from arcan_core.arcanx.arcanx_service import ArcanXService
from arcan_core.shadowodds.shadowodds_service import ShadowOddsService
from arcan_core.modules.modules_service import ModulesService

app = FastAPI(
    title="ArcanApp Backend",
    description="API pour ArcanX, ShadowOdds et les modules d'ArcanApp",
    version="1.0.0"
)

# Initialiser les services
arcanx_service = ArcanXService()
shadowodds_service = ShadowOddsService()
modules_service = ModulesService()

@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok", "message": "ArcanApp API fonctionne !"}

@app.post("/arcanx/analyze")
async def analyze_arcanx(data: dict):
    try:
        result = arcanx_service.run_analysis(data)
        return {"success": True, "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/shadowodds/analyze")
async def analyze_shadowodds(odds_data: dict):
    try:
        result = shadowodds_service.analyze_odds_behavior(odds_data)
        return {"success": True, "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/modules/activate")
async def activate_module(module_name: str):
    try:
        modules_service.activate_module(module_name)
        return {"success": True, "message": f"Module {module_name} activé"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/modules/deactivate")
async def deactivate_module(module_name: str):
    try:
        modules_service.deactivate_module(module_name)
        return {"success": True, "message": f"Module {module_name} désactivé"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
