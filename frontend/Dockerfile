FROM node:18-alpine

WORKDIR /app

COPY package.json /app/package.json
COPY public /app/public
COPY src /app/src

RUN npm install

EXPOSE 3000
CMD ["npm", "start"]