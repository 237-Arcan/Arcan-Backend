import os
from graphviz import Digraph

OUTPUT_DIR = "arcanapp/architecture_diagrams"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_dataflow_graph():
    g = Digraph("ArcanAppDataFlow", format="png")
    g.attr(rankdir='LR')

    g.node("Input", "Match/Event Input", shape="oval")
    g.node("ArcanX", "ArcanX Analyzer")
    g.node("ShadowOdds", "ShadowOdds Monitor")
    g.node("Sentinel", "Sentinel Live Core")
    g.node("DGrid", "D-GridSync", shape="component")
    g.node("Dashboard", "Realtime Dashboard", shape="folder")

    g.edges([
        ("Input", "ArcanX"),
        ("ArcanX", "ShadowOdds"),
        ("ShadowOdds", "Sentinel"),
        ("Sentinel", "Dashboard"),
        ("DGrid", "ArcanX"),
        ("DGrid", "ShadowOdds"),
        ("DGrid", "Sentinel")
    ])

    g.render(os.path.join(OUTPUT_DIR, "dataflow_graph"), cleanup=True)

def generate_modes_graph():
    g = Digraph("ModesRelation", format="png")
    g.attr(rankdir="TB")

    g.node("Start", "User Input / Match Trigger", shape="oval")
    g.node("Prediction", "Prediction Mode")
    g.node("Statistic", "Statistic Mode")
    g.node("Live", "Live Mode")
    g.node("Fusion", "ArcanBrain Fusion Engine")

    g.edge("Start", "Prediction")
    g.edge("Start", "Statistic")
    g.edge("Start", "Live")
    g.edge("Prediction", "Fusion")
    g.edge("Live", "Fusion")
    g.edge("Statistic", "Fusion")

    g.render(os.path.join(OUTPUT_DIR, "modes_graph"), cleanup=True)

def generate_arcanshadow_modules_graph():
    g = Digraph("ArcanShadowModules", format="png")
    g.attr(rankdir='LR')

    g.node("Sentinel", "Sentinel Live Mode", shape="box3d")
    g.node("ShadowCore", "ShadowOdds Core", shape="component")
    g.node("ChronoEcho", "ChronoEcho", shape="box")
    g.node("CollapseDetector", "CollapseDetector", shape="box")
    g.node("ClutchTimeScanner", "ClutchTimeScanner", shape="box")
    g.node("CrowdPressureIndex", "CrowdPressureIndex", shape="box")
    g.node("LateSurgeDetector", "LateSurgeDetector", shape="box")
    g.node("YouthImpactAnalyzer", "YouthImpactAnalyzer", shape="box")
    g.node("MomentumShiftTracker", "MomentumShiftTracker", shape="box")
    g.node("SetPieceThreatEvaluator", "SetPieceThreatEvaluator", shape="box")
    g.node("FanSentimentMonitor", "FanSentimentMonitor", shape="box")
    g.node("CaptainSwitch", "CaptainSwitch", shape="box")
    g.node("KarmicFlow", "KarmicFlow+", shape="box")

    # Relations
    g.edge("ShadowCore", "ChronoEcho")
    g.edge("ShadowCore", "CollapseDetector")
    g.edge("ShadowCore", "ClutchTimeScanner")
    g.edge("ShadowCore", "CrowdPressureIndex")
    g.edge("ShadowCore", "LateSurgeDetector")
    g.edge("ShadowCore", "YouthImpactAnalyzer")
    g.edge("ShadowCore", "MomentumShiftTracker")
    g.edge("ShadowCore", "SetPieceThreatEvaluator")
    g.edge("ShadowCore", "FanSentimentMonitor")
    g.edge("ShadowCore", "CaptainSwitch")
    g.edge("ShadowCore", "KarmicFlow")
    g.edge("ShadowCore", "Sentinel")

    g.render(os.path.join(OUTPUT_DIR, "arcanshadow_modules"), cleanup=True)

if __name__ == "__main__":
    generate_dataflow_graph()
    generate_modes_graph()
    generate_arcanshadow_modules_graph()
    print("Diagrammes générés dans :", OUTPUT_DIR)
