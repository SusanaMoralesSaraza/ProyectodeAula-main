CREATE TABLE if not exists public.creditos (
  nombre VARCHAR PRIMARY KEY,
  monto_credito INTEGER NOT NULL,
  duracion_periodo_meses INTEGER NOT NULL,
  tasa_interes_anual DECIMAL(5,2) NOT NULL,
  plazo_amortizacion INTEGER NOT NULL
);


DELETE FROM creditos  

