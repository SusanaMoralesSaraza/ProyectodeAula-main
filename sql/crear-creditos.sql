CREATE TABLE IF NOT EXISTS public.creditos (
  nombre VARCHAR(100) PRIMARY KEY,
  monto_credito INTEGER NOT NULL,
  duracion_periodo_meses INTEGER NOT NULL,
  tasa_interes_anual DECIMAL(5,2) NOT NULL,
  plazo_amortizacion INTEGER NOT NULL
);  

