import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'BancoDeDados.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE Marcas (
    marc_id INT AUTO_INCREMENT PRIMARY KEY,
    marc_nome VARCHAR(255) NOT NULL
);
""")

cursor.execute("""
CREATE TABLE Produtos (
    prod_id INT AUTO_INCREMENT PRIMARY KEY,
    prod_nome VARCHAR(255) NOT NULL,
    EAN VARCHAR(13) NOT NULL,
    fk_marc_id INT,
    FOREIGN KEY (fk_marc_id) REFERENCES Marcas(marc_id)
);
""")

cursor.execute("""
CREATE TABLE Estoque_De_chegada (
    prod_id INT,
    prod_nome VARCHAR(255),
    EAN VARCHAR(13),
    fk_marc_id INT,
    qtd INT,
    FOREIGN KEY (fk_marc_id) REFERENCES Marcas(marc_id),
    PRIMARY KEY (prod_id)
);
""")

cursor.execute("""
CREATE TABLE Estoque (
    fk_prod_nome VARCHAR(255),
    fk_marc_id INT,
    fk_prod_id INT,
    fk_EAN VARCHAR(13),
    qtd INT,
    FOREIGN KEY (fk_prod_id) REFERENCES Produtos(prod_id),
    FOREIGN KEY (fk_marc_id) REFERENCES Marcas(marc_id)
);
""")
connection.commit()

# Inserindo dados de exemplo
cursor.execute("INSERT INTO Marcas (marc_nome) VALUES ('Marca A'), ('Marca B');")
cursor.execute("""
INSERT INTO Produtos (prod_nome, EAN, fk_marc_id) VALUES
('Produto 1', '1234567890123', 1),
('Produto 2', '1234567890124', 1),
('Produto 3', '1234567890125', 2);
""")
connection.commit()

cursor.execute("""
INSERT INTO Estoque_De_chegada (prod_id, prod_nome, EAN, fk_marc_id, qtd) VALUES
(1, 'Produto 1', '1234567890123', 1, 50),
(2, 'Produto 2', '1234567890124', 1, 30),
(3, 'Produto 3', '1234567890125', 2, 20);
""")
connection.commit()

# Exemplo de inserção inicial no estoque
cursor.execute("""
INSERT INTO Estoque (fk_prod_nome, fk_marc_id, fk_prod_id, fk_EAN, qtd) VALUES
('Produto 1', 1, 1, '1234567890123', 100),
('Produto 2', 1, 2, '1234567890124', 150),
('Produto 3', 2, 3, '1234567890125', 200);
""")
connection.commit()

cursor.close()
connection.close()