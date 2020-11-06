from custom_logger import Employee
from custom_logger import custom_logger
import logging

#  USING Default log levels
log = custom_logger()
# log.info("Test INFO")
# log.debug("Test DEBUG")
# log.warning("Test warning")
# log.exception("Test exception")
# log.error("Test Error")
# log.critical("Test critical\n\n")
# #  change log level to INFO

# log.setLevel(logging.INFO)
# log.info("Test2 INFO")
# log.debug("Test2 DEBUG")
# log.warning("Test2 warning")
# log.exception("Test2 exception")
# log.error("Test2 Error")
# log.critical("Test2 critical\n\n")

# log.setLevel(logging.WARNING)
# log.info("Test3 INFO")
# log.debug("Test3 DEBUG")
# log.warning("Test3 warning")
# log.exception("Test3 exception")
# log.error("Test3 Error")
# log.critical("Test3 critical\n\n")

# log.setLevel(logging.ERROR)
# log.info("Test4 INFO")
# log.debug("Test4 DEBUG")
# log.warning("Test4 warning")
# log.exception("Test4 exception")
# log.error("Test4 Error")
# log.critical("Test4 critical\n\n")

# log.setLevel(logging.CRITICAL)
# log.info("Test5 INFO")
# log.debug("Test5 DEBUG")
# log.warning("Test5 warning")
# log.exception("Test5 exception")
# log.error("Test5 Error")
# log.critical("Test5 critical\n\n")

# log.setLevel(logging.DEBUG)
# log.info("Test6 INFO")
# log.debug("Test6 DEBUG")
# log.warning("Test6 warning")
# log.exception("Test6 exception")
# log.error("Test6 Error")
# log.critical("Test6 critical\n\n")

tc_status = "FAIL"

log.setLevel(logging.DEBUG)
if tc_status == 'PASS':
	log.info("test passed")
	log.warning("test warning")
	log.info("OTC-231.3 PASSED")
else:
	log.exception('test failed')
	log.info("OTC-231.3 PASSED")
