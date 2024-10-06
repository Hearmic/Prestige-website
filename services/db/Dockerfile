FROM postgres:15

# Set environment variables
ENV POSTGRES_DB prestige_database
ENV POSTGRES_USER ${POSTGRES_USER}
ENV POSTGRES_PASSWORD ${POSTGRES_PASSWORD}

# Create the database on container startup
RUN psql -c "CREATE DATABASE prestige_database" -U ${POSTGRES_USER}

# Expose the port for connections
EXPOSE 5432
