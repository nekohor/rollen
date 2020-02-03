import pondo

record_type = "ledger"
protocol_type = "tcp"

factor_names = ["asym_flt", "sym_flt"]
factor_names = ["wr_speed7"]

line = 2250

start_date = 20191225
end_date = 20191231

pondo.batch_export(factor_names, record_type, protocol_type,
                   line, start_date, end_date)
