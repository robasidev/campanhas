import re

# Abre o HTML original
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# =========================================================
# CONFIGURAÇÃO ÚNICA: Cole aqui os links de afiliado
# =========================================================
LINK_PRODUTOR = "https://pay.hotmart.com/O62694627R?checkoutMode=10&utm_source=organic&utm_campaign=&utm_medium=&utm_content=&utm_term=&xcod=&sck="
SEU_LINK_AFILIADO = "https://go.hotmart.com/S105998332R?ap=4ae5"
# =========================================================

# 1. Troca o link de afiliado (caso o link antigo mude)
if LINK_PRODUTOR:
    html = html.replace(LINK_PRODUTOR, SEU_LINK_AFILIADO)

# 2. LIMPEZA UNIVERSAL DE BOTÕES DE ROLAGEM (Qualquer página)
# Esse Regex localiza TODOS os links que começam com # (ex: href="#qualquer-coisa")
# e limpa os atributos que fazem abrir nova aba ou travar a rolagem, mantendo as classes.
padrao_ancora = r'(<a[^>]*href=["\'](#[^"\']+)["\'][^>]*>)'

def limpar_atributos_botao(match):
    tag_completa = match.group(1)
    # Remove o target="_blank" se existir
    tag_limpa = re.sub(r'target=["\']_blank["\']', '', tag_completa)
    # Remove os comandos de clique do OptimizePress/outros construtores
    tag_limpa = re.sub(r'data-op-[a-zA-Z0-9-]+=["\'][^"\']*["\']', '', tag_limpa)
    tag_limpa = re.sub(r'data-op3-[a-zA-Z0-9-]+=["\'][^"\']*["\']', '', tag_limpa)
    return tag_limpa

html = re.sub(padrao_ancora, limpar_atributos_botao, html)

# 3. FORÇAR ROLAGEM SUAVE (Injeção prioritária no CSS)
# Coloca o estilo no início do bloco de CSS para garantir que o navegador leia
estilo_smooth = "\nhtml { scroll-behavior: smooth !important; }\n"
html = html.replace("</style>", estilo_smooth + "</style>", 1)

# Salva o arquivo final
with open("index_pronto.html", "w", encoding="utf-8") as f:
    f.write(html)

print("🚀 Automação concluída! Arquivo 'index_pronto.html' gerado com rolagem suave forçada.")