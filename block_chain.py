import hashlib
import json
from time import time

class Block:
    """Representa un único bloque en la cadena de bloques."""
    def __init__(self, index, timestamp, data, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Calcula el hash SHA-256 del contenido del bloque."""
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        
        return hashlib.sha256(block_string).hexdigest()

    def __repr__(self):
        """Representación amigable del bloque."""
        return f"Block(Index: {self.index}, Hash: {self.hash[:15]}..., Nonce: {self.nonce})"

class Blockchain:
    """Gestiona la cadena de bloques, las transacciones y la minería."""
    
    DIFFICULTY_TARGET = "0000" 
    
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """Crea el primer bloque de la cadena (índice 0)."""
        self.create_new_block(
            nonce=1,
            previous_hash="0",
            data=[{"sender": "System", "recipient": "Genesis", "amount": 0}]
        )

    @property
    def last_block(self):
        """Devuelve el último bloque en la cadena."""
        return self.chain[-1]

    def create_new_block(self, nonce, previous_hash, data):
        """Crea un nuevo bloque, calcula su hash y lo añade a la cadena."""
        block = Block(
            index=len(self.chain),
            timestamp=time(),
            data=data,
            previous_hash=previous_hash,
            nonce=nonce
        )
        block.hash = block.calculate_hash()
        
        self.chain.append(block)
        return block

    def proof_of_work(self, last_hash):
        """
        Algoritmo simple de Prueba de Trabajo (PoW).
        Busca un 'nonce' para que el nuevo hash cumpla con la dificultad.
        """
        nonce = 0
        while True:
            
            guess = f'{last_hash}{nonce}'.encode()
            guess_hash = hashlib.sha256(guess).hexdigest()
            
            if guess_hash[:len(self.DIFFICULTY_TARGET)] == self.DIFFICULTY_TARGET:
                return nonce
            nonce += 1
    
    def mine_pending_transactions(self, miner_address):
        """
        Ejecuta la minería: corre el PoW y crea el nuevo bloque.
        """
        transactions_to_mine = list(self.pending_transactions)
        
        print(f"\n[INFO] Minando Bloque #{len(self.chain)}...")
        last_block = self.last_block
        nonce = self.proof_of_work(last_block.hash)
        
        new_block = self.create_new_block(
            nonce=nonce,
            previous_hash=last_block.hash,
            data=transactions_to_mine
        )
        
        print(f"¡Bloque Minado! Index: {new_block.index}, Nonce: {new_block.nonce}, Hash: {new_block.hash[:15]}...")
        
        self.pending_transactions = []
        self.add_transaction(
            sender="0 (System Reward)", 
            recipient=miner_address, 
            amount=1.0 # Recompensa
        )
        
        print(f"[INFO] Recompensa de 1.0 para {miner_address} añadida a transacciones pendientes.")
        return new_block

    def add_transaction(self, sender, recipient, amount):
        """Crea una nueva transacción y la añade a la lista de pendientes."""
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            'timestamp': time()
        }
        self.pending_transactions.append(transaction)
        return self.last_block.index + 1

    def is_chain_valid(self):
        """Verifica la integridad de toda la cadena (hash y previous_hash)."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                print(f"[ERROR] Hash de Bloque #{current_block.index} inválido.")
                return False

            if current_block.previous_hash != previous_block.hash:
                print(f"[ERROR] Vínculo de Bloque #{current_block.index} roto (hash anterior no coincide).")
                return False
                
        return True

if __name__ == '__main__':
    
    MINER_ADDRESS = "GHCoderAddress"
    
    my_blockchain = Blockchain()
    print("--- ⚙️ CADENA INICIALIZADA ---")
    print(f"Bloque Génesis: {my_blockchain.chain[0]}")
    print("-" * 50)

    print("--- 💰 AÑADIENDO TRANSACCIONES ---")
    my_blockchain.add_transaction("Alice", "Bob", 10.5)
    my_blockchain.add_transaction("Carol", "David", 5.0)
    print(f"Total de transacciones pendientes: {len(my_blockchain.pending_transactions)}")
    print("-" * 50)

    my_blockchain.mine_pending_transactions(miner_address=MINER_ADDRESS)
    print("-" * 50)

    my_blockchain.add_transaction("Eve", "Frank", 2.2)
    print(f"Total de transacciones pendientes: {len(my_blockchain.pending_transactions)}")
    print("-" * 50)

    my_blockchain.mine_pending_transactions(miner_address=MINER_ADDRESS)
    print("-" * 50)

    print("\n--- ✅ RESUMEN DE LA CADENA ---")
    for block in my_blockchain.chain:
        print(f"[{block.index}] {block.hash[:32]}... | Nonce: {block.nonce}")
        if block.index > 0:
            print(f"    Datos Minados: {len(block.data)} Transacciones") 
        else:
             print(f"    Datos: Bloque Génesis")
            
    print("-" * 50)
    print(f"Validación de la Cadena: {'VÁLIDA' if my_blockchain.is_chain_valid() else 'INVÁLIDA'}")
    
    print("\n--- 🚨 DEMOSTRACIÓN DE MANIPULACIÓN (INMUTABILIDAD) ---")
    my_blockchain.chain[1].data.append({"manipulated": True})
    my_blockchain.chain[1].hash = my_blockchain.chain[1].calculate_hash() 

    print("El Bloque 1 ha sido manipulado y su hash recalculado.")
    print(f"Validación de la Cadena (Post-Manipulación): {'VÁLIDA' if my_blockchain.is_chain_valid() else 'INVÁLIDA'}")
