FROM node:current-buster as development

WORKDIR /usr/src/app

COPY ./server/package*.json ./

RUN yarn install --only=development

COPY ./server .

COPY ./server /usr/src/app/

RUN yarn run build

FROM node:current-buster as production

ARG NODE_ENV=production
ENV NODE_ENV=${NODE_ENV}

WORKDIR /usr/src/app/

COPY ./server/package*.json ./

RUN yarn install --only=production

COPY ./server .

COPY --from=development /usr/src/app/dist ./dist

CMD ["node", "dist/main"]