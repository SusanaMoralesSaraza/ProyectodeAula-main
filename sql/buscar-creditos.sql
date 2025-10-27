SELECT nombre,
monto_credito, 
duracion_periodo_meses,
tasa_interes_anual,
plazo_amortizacion
FROM public.creditos;
LIMIT 1000;

INSERT INTO creditos (nombre, monto_credito, duracion_periodo_meses, tasa_interes_anual, plazo_amortizacion)
VALUES ('Felipe', 25000000, 72, 12, 140);

where duracion_periodo_meses = 72;

