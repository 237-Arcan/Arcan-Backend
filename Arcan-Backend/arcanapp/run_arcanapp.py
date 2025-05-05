from arcanapp.core.orchestrator import Orchestrator
import argparse

def main():
    parser = argparse.ArgumentParser(description="ArcanApp Multi-Mode Launcher")
    parser.add_argument("--mode", type=str, required=True, help="Mode à lancer: prediction / live / statistics")
    args = parser.parse_args()

    orchestrator = Orchestrator()

    if args.mode == "prediction":
        orchestrator.run_prediction_mode()
    elif args.mode == "live":
        orchestrator.run_live_analysis_mode()
    elif args.mode == "statistics":
        orchestrator.run_statistic_mode()
    else:
        print(f"Mode inconnu : {args.mode}")

if __name__ == "__main__":
    main()
