"""Restaura os objetos do remote DVC local a partir de uma release do projeto."""

from hashlib import sha256
from io import BytesIO
from pathlib import Path
from urllib.request import Request, urlopen
from zipfile import ZipFile

URL = (
    "https://github.com/Rafaela091/aula-05-dvc-lab/releases/"
    "download/dvc-cache-v1/aula05-dvc-cache.zip"
)
EXPECTED_SHA256 = "77cd53d755fa3ce9349f2661c82d9fc584c6d2ef139d39863001e20ffb77168a"
ROOT = Path(__file__).resolve().parents[1]


def main():
    request = Request(URL, headers={"User-Agent": "aula05-dvc-lab"})
    with urlopen(request, timeout=60) as response:
        payload = response.read()
    digest = sha256(payload).hexdigest()
    if digest != EXPECTED_SHA256:
        raise ValueError(f"SHA-256 inesperado: {digest}")

    count = 0
    with ZipFile(BytesIO(payload)) as archive:
        for member in archive.infolist():
            parts = Path(member.filename).parts
            if not parts or parts[0] != "remote_storage" or ".." in parts:
                raise ValueError(f"Caminho inválido no arquivo: {member.filename}")
            destination = ROOT.joinpath(*parts)
            if member.is_dir():
                destination.mkdir(parents=True, exist_ok=True)
                continue
            destination.parent.mkdir(parents=True, exist_ok=True)
            with archive.open(member) as source, destination.open("wb") as target:
                target.write(source.read())
            count += 1
    print(f"Remote local restaurado: {count} objetos em {ROOT / 'remote_storage'}")
    print("Agora execute: dvc pull")


if __name__ == "__main__":
    main()
