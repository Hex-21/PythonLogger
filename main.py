import logger

logger = logger.setup_logger(file_name=f"./Log.log")
logger.debug(f"Logger initialized: {logger}")
logger.info(f"Logger initialized: {logger}")
logger.warning(f"Logger initialized: {logger}")
logger.error(f"Logger initialized: {logger}")
logger.critical(f"Logger initialized: {logger}")
exit(0)
