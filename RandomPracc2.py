# Crie um programa que pergunte ao funcionário qual produto o cliente comprou de acordo com o valor inserido pelo funcionario
# onde terá o valor de cada produto, o programa deve fazer a soma dos produtos e retornar o valor total da venda
# após isso o programa deve perguntar ao funcionário se o mesmo deseja aplicar % de desconto sobre o valor total 
# e retornar o valor total atualizado da venda, após isso deve-se perguntar qual a forma de pagamento, se for pix ou dinheiro (desconto aplicável)
# agora, se for cartão de débito ou crédito (desconto não aplicável)

from multiprocessing import Value
import os

if __name__ == '__main__':

    def sellProducts():
        products = {
            'drink' : 50,
            'whisky' : 180,
            'gin' : 140,
            'cerveja' : 40
            }

        aliases = {
            'w': 'whisky',
            'whisk': 'whisky',
            'd' : 'drink',
            'g': 'gin',
            'beer': 'cerveja',
        }
        cart = []
        totalValue = 0
           
        print(f'Olá, bem vindo ao sistema Deivin SportBar\n')
        while True:
            print(f'Produtos disponíveis: ')
            for name, price in products.items(): # Exibindo produtos disponíveis
                print(f'Produto: {name}: | Preço {price:.2f} R$')    
            
            sell = input(f'Por favor selecione o produto vendido: ').strip().lower()
            if sell in aliases: # Checando aliases
                sell = aliases.get(sell, sell) # Aplica alias se existir
            
            if sell not in products:
                print(f'Digite um produto válido')
                continue
            
            while True:
                quantityString = input(f'\nQuantidade: ')
                try:
                    quantity = int(quantityString)
                except ValueError:
                    print(f'Digite um número inteiro válido')
                    continue
                if quantity <= 0:
                    print(f'A quantidade deve ser maior que ZERO\n')
                    continue
                break
            
            # Calculando valor parcial e adicionar ao carrinho
            price = products[sell]
            parcialValue = price * quantity

            cart.append({
                'nome' : sell,
                'preco_unitario' : price,
                'quantidade' : quantity,
                'valor' : parcialValue
            })
            totalValue += parcialValue
            print(f'Adicionado: {sell} x {quantity} - Total: {totalValue} R$')
            print(f'\nValor do carrinho atual: {totalValue:.2f} R$\n')

        # Perguntando se deseja adicionar outro produto        
        
            answerSell = input(f'Deseja adicionar outro produto? (S/N)').strip().lower()
            if answerSell in ["n", "no","nao", "não"]:
                break
            elif answerSell in ["s", "y", "sim", "yes"]:
                continue
            else:
                print(f'Resposta inválida, irei considerar que você não deseja adicionar outro produto!')
                break
        
        # Se não houver itens, finalizar venda
        if not cart:
            print(f'Nenhum produto adicionado. Finalizando venda.')
            return


        discountPerc = 0.0
        answerDiscount = input(f'Deseja aplicar desconto? (S/N) ').strip().lower()
        if answerDiscount in ['s', 'y', 'sim', 'yes']:
            while True:
                discountString = input(f'Digite o % de desconto (0 a 20): ').strip()
                try:
                    discountPerc = float(discountString.replace(',', '.'))
                except ValueError:
                    print(f'Digite um percentual válido (ex: 5, 10, 12.5)!')
                    continue

                if not (0 <= discountPerc <= 20):
                    print(f'O desconto deve estar entre 0% e 20%...')
                    continue
                break

            # Forma de pagamento e aplicabilidade do desconto

            paymentMethod = input(f'Qual a forma de pagamento? (pix/dinheiro/debito/credito) -> ').strip().lower()
            applyDiscount = paymentMethod in ['pix', 'dinheiro']

            if applyDiscount:
                valueDiscount = totalValue * (discountPerc / 100.0)
                totallyFinal = totalValue - valueDiscount
            else:
                if discountPerc > 0:
                    print(f'Desconto informado, porém NÃO aplicável para débito/crédito. Total segue sem desconto.')
                    valueDiscount = 0.0
                    totallyFinal = totalValue

        # Resumo da venda
        print(f'--- Itens comprado ---\n')
        for item in cart:
            print(
                f"{item['nome']} x {item['quantidade']} | "
                f"Unitário: R$ {item['preco_unitario']:.2f} | "
                f"Subtotal: R$ {item['valor']:.2f}"
            )

        print(f' -------------------------- ')
        print(f'Total bruto: {totalValue:.2f} R$')
        print(f'Desconto: ({discountPerc:.2f}%): {valueDiscount:.2f} R$')
        print(f'Forma de pagamento: {paymentMethod.upper()}')
        print(f'Valor a ser pago: {totallyFinal:.2f} R$')
        print(f'Agradeça o cliente pela preferência em nos escolher!')

sellProducts()