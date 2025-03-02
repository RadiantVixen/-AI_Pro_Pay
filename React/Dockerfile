# Use an official Node.js runtime as the base image
FROM node:16

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json (or yarn.lock)
COPY package.json yarn.lock ./

# Install dependencies
RUN yarn install
RUN npm install axios tailwindcss @stripe/react-stripe-js @stripe/stripe-js

# Copy the rest of the application code
COPY . .

# Expose port 3000 (default for React apps)
EXPOSE 3000

# Start the React app
CMD ["yarn", "start", "--", "--open"]


