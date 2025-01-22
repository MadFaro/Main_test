TRUNC(dt, 'HH24') + FLOOR(TO_CHAR(dt, 'MI') / 30) * (30 / 1440)
