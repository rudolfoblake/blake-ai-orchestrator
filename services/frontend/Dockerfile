FROM node:18-alpine

WORKDIR /app

COPY services/frontend/package.json /app/package.json
COPY services/frontend/public /app/public
COPY services/frontend/src /app/src

RUN npm install

EXPOSE 3000
CMD ["npm", "start"]