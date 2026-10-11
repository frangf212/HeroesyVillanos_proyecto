import logging
from pathlib import Path


carpeta_actual = Path(__file__).resolve().parent
raiz = carpeta_actual.parent
directoriologs= raiz / "logs"
rutalogs=directoriologs/"app.log"

directoriologs.mkdir(exist_ok=True)



logging.basicConfig(
    filename=rutalogs,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8",
)

logger = logging.getLogger("heroes_villanos")