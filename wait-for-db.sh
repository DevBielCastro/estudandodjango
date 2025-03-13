#!/bin/sh

host="$1"
port="$2"
shift 2

while ! nc -z "$host" "$port"; do
  echo "Aguardando MySQL em $host:$port..."
  sleep 2
done

echo "MySQL pronto! Executando comando: $@"
exec "$@"
