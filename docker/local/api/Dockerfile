FROM python:3.14-slim-bookworm
LABEL authors="Ashish"

# argument for  directory, user group, user
ARG HOME_DIR=/todo
ARG GROUP=todo
ARG USER=todo

WORKDIR ${HOME_DIR}

RUN groupadd -r ${GROUP} \
    && useradd -r -g ${GROUP} -d ${HOME_DIR} -m ${USER}

COPY --chown=${USER}:${GROUP} . ${HOME_DIR}

COPY requirements.txt  .

RUN --mount=type=bind,from=wheels,source=/,target=/wheels \
    pip install --no-index --find-links=/wheels -r requirements.txt

RUN chmod +x ${HOME_DIR}/scripts/entrypoint.sh


USER ${APP_USER}

ENTRYPOINT ["scripts/entrypoint.sh"]