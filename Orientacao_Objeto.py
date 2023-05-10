def criarconta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite":limite}
    return conta
conta = criarconta(123, "chris", 55, 100)
print(conta["titular"])


def deposita(conta, valor):
    conta["saldo"] += valor


def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("saldo é {}".format(conta["saldo"]))


deposita(conta,15.0)
print(extrato(conta))

saca(conta, 15.0)
print(extrato(conta))