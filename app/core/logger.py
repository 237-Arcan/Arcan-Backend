import logging

# Configuration du logger
logging.basicConfig(
    filename='arcan_decisions.log',
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def log_decision(module_name, context, result):
    logging.info(f"Module: {module_name} | Context: {context} | Result: {result}")
