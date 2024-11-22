# Usa uma imagem Node.js oficial como base para construir a aplicação
#FROM node:18-alpine AS build

FROM node:22.11-alpine3.19 AS build

# RUN npm init
# WORKDIR /app
# WORKDIR /app/frontend/frontend
# RUN npm install @babel/plugin-proposal-private-property-in-object --save-dev
# RUN npm install webpack@latest webpack-dev-server@latest react-scripts@latest --save-dev
RUN apk update && apk add --no-cache netcat-openbsd
COPY app/package.json ./
COPY app/package-lock.json ./
# COPY package.json ./
# COPY package.json ./
# RUN npm install --force --loglevel verbose

# RUN npm install --force --loglevel verbose

# RUN npm ci --force --loglevel verbose
RUN npm ci --force --loglevel verbose

# RUN npm install webpack-dev-server@latest --save-dev
# RUN npm install @babel/plugin-proposal-private-property-in-object --save-dev
# #--force --loglevel verbose
# COPY public /public
# RUN ls
# Usa uma imagem Nginx para servir a aplicação
# FROM nginx:stable-alpine
# COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 3000
# CMD ["cd", "/frontend", "&&", "ls"]
# CMD ["sh", "-c", "ls"]
# CMD ["npm", "start"]