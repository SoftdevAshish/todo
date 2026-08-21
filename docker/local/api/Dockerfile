FROM python:3.14-slim-bookworm
LABEL authors="Ashish"

# argument for  directory, user group, user
ARG HOME_DIR=/todo
ARG GROUP=todos
ARG USER=todos

WORKDIR ${HOME_DIR}

RUN groupadd -r ${GROUP} \
    && useradd -r -g ${GROUP} -d ${HOME_DIR} -m ${USER}




COPY requirements.txt  .

RUN --mount=type=bind,from=wheels,source=/,target=/wheels \
    pip install --no-index --find-links=/wheels -r requirements.txt

COPY --chown=${USER}:${GROUP} . ${HOME_DIR}


RUN mkdir -p ${HOME_DIR}/logs && \
  chown -R ${USER}:${GROUP} ${HOME_DIR}/logs && \
  chmod 777 ${HOME_DIR}/logs


RUN chmod +x scripts/entrypoint.sh



USER ${USER}

ENTRYPOINT ["scripts/entrypoint.sh"]