SELECT nombre,
monto_credito, 
duracion_periodo_meses,
tasa_interes_anual,
plazo_amortizacion
FROM public.creditos;


INSERT INTO creditos (nombre, monto_credito, duracion_periodo_meses, tasa_interes_anual, plazo_amortizacion)
VALUES ('Maria', 20000000, 60, 12, 120);

where duracion_periodo_meses = 72;

