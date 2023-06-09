import yaml
from gate_api import Configuration

def load_creds(file):
	with open(file) as file:
		auth = yaml.load(file,  Loader=yaml.FullLoader)

#	return Configuration(key=auth["gateio_api"], secret=auth["gateio_secret"])
	return Configuration(host = "https://api.gateio.ws/api/v4", key=auth["gateio_api"], secret=auth["gateio_secret"])

