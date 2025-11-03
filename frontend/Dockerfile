FROM node:18-alpine

WORKDIR /app

COPY frontend/package.json /app/package.json
COPY frontend/public /app/public
COPY frontend/src /app/src

RUN npm install

EXPOSE 3000
CMD ["npm", "start"]