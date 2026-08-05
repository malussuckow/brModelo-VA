# corretorXml

> (pt-BR) Corretor automático de diagramas Entidade-Relacionamento (ER) baseado em similaridade léxica, semântica e estrutural.

> (en-US) Automatic corrector for Entity-Relationship (ER) diagrams based on lexical, semantic, and structural similarity.

---

## (pt-BR) Português

### 📌 Sobre o projeto

O **corretorXml** é uma aplicação Django que compara dois esquemas conceituais Entidade-Relacionamento (ER), exportados em XML pelo **brModelo**, e calcula automaticamente o quão parecido o esquema de um aluno é em relação ao gabarito definido por um professor.

O projeto foi desenvolvido no âmbito de um projeto de pesquisa do curso de Sistemas de Informação, com o objetivo de automatizar parte da correção de exercícios de modelagem de dados, uma tarefa que hoje é feita manualmente e de forma subjetiva.

### ✨ Funcionalidades

- Upload de arquivos XML de esquemas ER (formato brModelo)
- Conversão do XML em um **grafo heterogêneo direcionado** (`NetworkX MultiDiGraph`), com entidades, atributos e relacionamentos representados como nós tipados
- **Similaridade léxica**: compara os nomes dos elementos caractere a caractere (RapidFuzz)
- **Similaridade semântica**: compara o *significado* dos nomes usando embeddings (sentence-transformers), capturando sinônimos que a comparação léxica não pega (ex: "cachorro" ↔ "cão")
- **Similaridade estrutural** *(em desenvolvimento)*: compara cardinalidades e a topologia das conexões entre entidades e relacionamentos
- Nota geral e notas detalhadas por categoria (entidades, relacionamentos, atributos), com o "match" encontrado para cada elemento
- Interface web para professores cadastrarem atividades e alunos submeterem seus esquemas

### 🏛️ Arquitetura

O projeto segue uma arquitetura modular, separando claramente cada responsabilidade:

```
corretor/
├── domain/          # Classes de domínio (Entity, Attribute, Relationship)
├── parser/          # Leitura do XML e construção do grafo
├── normalization/   # Normalização textual (acentos, minúsculas, singularização)
├── similarity/      # Similaridade léxica, semântica e estrutural
└── services/        # Orquestração do pipeline completo (logic_service)
```

O pipeline segue este fluxo:

```
XML (brModelo) → Parser → Grafo tipado (NetworkX) → Normalização
→ Similaridade (léxica + semântica) → Combinação → Nota final
```

### 🛠️ Tecnologias

| Camada | Ferramenta |
|---|---|
| Backend | Python 3.11+, Django |
| Grafos | NetworkX (`MultiDiGraph`) |
| Similaridade léxica | RapidFuzz |
| Similaridade semântica | sentence-transformers (`all-MiniLM-L6-v2`) |
| Parsing XML | `xml.etree.ElementTree` |

### ⚠️ Limitações conhecidas

Modelos de embeddings genéricos (sentence-transformers, spaCy) têm dificuldade em capturar sinônimos de domínio muito específico que não aparecem com frequência em seus dados de treino (ex: "dono" ↔ "tutor" em contextos de veterinária). Essa é uma limitação documentada da área de NLP, não uma falha do sistema,e um dos pontos de evolução futura do projeto.

### 🚀 Rodando localmente

```bash
git clone https://github.com/seu-usuario/corretorXml.git
cd corretorXml
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### 🗺️ Roadmap

- [x] Parser XML (brModelo)
- [x] Construção do grafo tipado
- [x] Similaridade léxica
- [x] Similaridade semântica
- [ ] Similaridade estrutural (cardinalidades)
- [ ] Similaridade topológica (Graph Edit Distance)
- [ ] Combinação ponderada de todas as métricas

---

## (en-US) English

### 📌 About
**corretorXml** is a Django application that compares two Entity-Relationship (ER) conceptual schemas exported as XML from **brModelo** and automatically calculates how closely a student's schema matches the instructor's reference schema.

The project was developed as part of an undergraduate research scholarship in the Information Systems program. The goal is to automate the assessment of ER modeling exercises, a process that is currently performed manually and subjectively.

### ✨ Features

- Upload of ER schema XML files (brModelo format)
- Conversion of XML into a **typed, directed heterogeneous graph** (`NetworkX MultiDiGraph`), with entities, attributes, and relationships represented as typed nodes
- **Lexical similarity**: compares element names character by character using RapidFuzz
- **Semantic similarity**: compares the *meaning* of names using sentence-transformers embeddings, identifying synonyms that lexical comparison may miss (e.g., "dog" ↔ "canine")
- **Structural similarity** *(in progress)*: compares cardinalities and the topology of connections between entities and relationships
- Overall score with detailed results for entities, relationships, and attributes, including the best match for each element
- Web interface for instructors to create assignments and for students to submit their schemas
  
### 🏛️ Architecture

The project follows a modular architecture with clearly separated responsibilities:

```
corretor/
├── domain/          # Domain classes (Entity, Attribute, Relationship)
├── parser/          # XML reading and graph construction
├── normalization/   # Text normalization (accents, lowercase, lemmatization)
├── similarity/      # Lexical, semantic, and structural similarity
└── services/        # Full pipeline orchestration (logic_service)
```

Pipeline overview:

```
XML (brModelo) → Parser → Typed graph (NetworkX) → Normalization
→ Similarity (lexical + semantic) → Combination → Final score
```

### 🛠️ Tech stack

| Layer | Tool |
|---|---|
| Backend | Python 3.11+, Django |
| Graphs | NetworkX (`MultiDiGraph`) |
| Lexical similarity | RapidFuzz |
| Semantic similarity | sentence-transformers (`all-MiniLM-L6-v2`) |
| XML parsing | `xml.etree.ElementTree` |

### ⚠️ Known limitations

General-purpose embedding models (sentence-transformers, spaCy) struggle to capture domain-specific synonyms that are underrepresented in their training data (e.g. "owner" ↔ "guardian" in a veterinary context). This is a well-documented limitation in NLP, not a system flaw,and one of the planned areas for future improvement.

### 🚀 Running locally

```bash
git clone https://github.com/your-username/corretorXml.git
cd corretorXml
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### 🗺️ Roadmap

- [x] XML parser (brModelo)
- [x] Typed graph construction
- [x] Lexical similarity
- [x] Semantic similarity
- [ ] Structural similarity (cardinalities)
- [ ] Topological similarity (Graph Edit Distance)
- [ ] Weighted combination of all metrics
