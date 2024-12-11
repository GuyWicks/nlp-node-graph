venv=.venv/bin
python=source ${venv}/activate && ${venv}/python
fastapi=source ${venv}/activate && ${venv}/fastapi
uvicorn=source ${venv}/activate && ${venv}/uvicorn

version:
	@${python} --version

install: install_packages spacy_install_model

install_packages: 
	@${python} -m pip install -r requirements.txt

spacy_install_model:
	@${python} -m spacy download en_core_web_sm
#	@${python} -m spacy download en_core_web_md
#	@${python} -m spacy download en_core_web_lg
#	@${python} -m spacy download en_core_web_trf
	@${python} -m spacy validate

spacy_uninstall_model:
	@${python} -m spacy pip uninstall en_core_web_sm
	@${python} -m spacy pip uninstall en_core_web_md
	@${python} -m spacy pip uninstall en_core_web_lg
	@${python} -m spacy pip uninstall en_core_web_trf
	@${python} -m spacy validate

spacy_clean:
	@${python} -m pip uninstall en_core_web_sm
	@${python} -m pip uninstall en_core_web_md

start:
	@${fastapi} dev  --port 8011
#	@${uvicorn} --port 8010 --reload --reload-delay 5 main:fastapi
