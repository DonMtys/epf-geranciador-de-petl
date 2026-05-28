"""Gera speed_lc840.html — Speed Round Certo/Errado 5s por questão"""

QUESTOES = [
    # POSSE / PROVIMENTO
    {"cat":"Provimento","q":"A posse deve ocorrer em até 30 dias após a publicação do ato de nomeação.","g":"C","art":"Art. 17, §1º","tip":"Posse = 30 dias. Não tomando posse, o ato é tornado sem efeito."},
    {"cat":"Provimento","q":"Após a posse, o servidor tem 10 dias úteis para entrar em exercício.","g":"E","art":"Art. 19, §2º","tip":"Exercício = 5 dias úteis (não 10)."},
    {"cat":"Provimento","q":"O estágio probatório tem duração de 3 anos de efetivo exercício.","g":"C","art":"Art. 22","tip":"Estágio probatório = 3 anos. Mesmo prazo da estabilidade."},
    {"cat":"Provimento","q":"A estabilidade é adquirida após 2 anos de efetivo exercício.","g":"E","art":"Art. 32","tip":"Estabilidade = 3 anos + aprovação na avaliação especial."},
    {"cat":"Provimento","q":"O concurso público tem validade de até 2 anos, prorrogável uma vez por igual período.","g":"C","art":"Art. 12","tip":"Validade máxima: 4 anos no total."},
    {"cat":"Provimento","q":"São reservadas 20% das vagas para candidatos com deficiência no concurso público.","g":"C","art":"Art. 13","tip":"PCD = 20%, desprezada a parte decimal."},
    {"cat":"Provimento","q":"Pelo menos 50% dos cargos em comissão devem ser ocupados por servidores de carreira.","g":"E","art":"Art. 10, §1º","tip":"O percentual correto é 70%, não 50%."},
    {"cat":"Provimento","q":"A posse em cargo público pode ser realizada por procurador com poderes específicos.","g":"C","art":"Art. 18, §3º","tip":"Posse por procuração: admitida com poderes expressos."},
    {"cat":"Provimento","q":"A nomeação é a única forma de provimento originário de cargo público.","g":"C","art":"Art. 7º, §1º","tip":"Todas as outras formas (reversão, reintegração etc.) são derivadas."},
    {"cat":"Provimento","q":"A recondução é o retorno do servidor estável ao cargo anterior por inabilitação no estágio probatório do novo cargo.","g":"C","art":"Art. 37","tip":"Recondução: inabilitação no estágio do novo cargo ou reintegração do anterior ocupante."},
    # RETORNO AO CARGO
    {"cat":"Retorno","q":"Na reversão, o servidor tem 15 dias úteis para retornar ao exercício após a comunicação.","g":"C","art":"Art. 34, §1º","tip":"Reversão = 15 dias úteis. Não confundir com reintegração (5 dias úteis)."},
    {"cat":"Retorno","q":"Na reintegração, o servidor tem 5 dias úteis para retornar ao exercício.","g":"C","art":"Art. 36, §3º","tip":"Reintegração = 5 dias úteis. Reversão = 15 dias úteis."},
    {"cat":"Retorno","q":"Na recondução, o servidor deve retornar no dia seguinte à ciência do ato.","g":"C","art":"Art. 37, §2º","tip":"Recondução = dia seguinte. O mais rápido de todos."},
    {"cat":"Retorno","q":"No aproveitamento (disponibilidade), o servidor tem 60 dias para retornar.","g":"E","art":"Art. 40, §1º","tip":"Aproveitamento = 30 dias (não 60)."},
    {"cat":"Retorno","q":"A reversão voluntária exige que tenham decorrido menos de 5 anos da aposentadoria.","g":"C","art":"Art. 34, III, b","tip":"Reversão voluntária: menos de 5 anos + cargo vago."},
    {"cat":"Retorno","q":"A remuneração na disponibilidade nunca pode ser inferior a 1/2 do que o servidor percebia.","g":"E","art":"Art. 38, §único","tip":"Disponibilidade: mínimo 1/3 (não 1/2)."},
    # JORNADA
    {"cat":"Jornada","q":"A jornada do servidor efetivo é de 30 horas semanais.","g":"C","art":"Art. 57","tip":"Efetivo = 30h. CC/FC = 40h."},
    {"cat":"Jornada","q":"O cargo em comissão tem jornada de 40 horas semanais.","g":"C","art":"Art. 58","tip":"CC = 40h com integral dedicação."},
    {"cat":"Jornada","q":"O serviço extraordinário é limitado a 4 horas por dia.","g":"E","art":"Art. 60","tip":"Extraordinário: limite de 2 horas por dia."},
    {"cat":"Jornada","q":"O adicional por serviço extraordinário é de 50% sobre a hora normal.","g":"C","art":"Art. 84","tip":"Hora extra = +50%."},
    {"cat":"Jornada","q":"O adicional noturno é de 25%, calculado sobre a hora normal.","g":"C","art":"Art. 85","tip":"Noturno = 25%. A hora noturna = 52min30s."},
    {"cat":"Jornada","q":"O abono de ponto corresponde a 5 dias por ano sem faltas injustificadas.","g":"C","art":"Art. 151","tip":"Abono de ponto = 5 dias."},
    {"cat":"Jornada","q":"O prazo para usar o abono de ponto extingue-se em 31 de dezembro do mesmo ano aquisitivo.","g":"E","art":"Art. 151, §2º","tip":"Extingue em 31/12 do ANO SEGUINTE ao aquisitivo."},
    # FÉRIAS
    {"cat":"Férias","q":"As férias têm duração de 30 dias a cada 12 meses de efetivo exercício.","g":"C","art":"Art. 125","tip":"Férias = 30 dias / 12 meses."},
    {"cat":"Férias","q":"As férias podem ser acumuladas em até 3 períodos por necessidade do serviço.","g":"E","art":"Art. 125, §4º","tip":"Acumulação máxima: 2 períodos."},
    {"cat":"Férias","q":"As férias podem ser parceladas em até 3 etapas, nenhuma inferior a 10 dias.","g":"C","art":"Art. 125, §5º","tip":"Parcelamento: até 3 etapas, mínimo 10 dias cada."},
    # FALTAS
    {"cat":"Faltas","q":"O abandono de cargo ocorre com ausência injustificada superior a 30 dias consecutivos.","g":"C","art":"Art. 64, I","tip":"Abandono = +30 dias consecutivos. Punição: demissão."},
    {"cat":"Faltas","q":"A inassiduidade habitual ocorre com ausência injustificada superior a 60 dias interpolados em 12 meses.","g":"C","art":"Art. 64, II","tip":"Inassiduidade = +60 dias interpolados em 12 meses."},
    {"cat":"Faltas","q":"O casamento garante ao servidor 8 dias consecutivos de ausência justificada.","g":"C","art":"Art. 62, III","tip":"Casamento/falecimento de familiar próximo = 8 dias consecutivos."},
    {"cat":"Faltas","q":"O alistamento eleitoral garante ao servidor 2 dias de ausência justificada.","g":"C","art":"Art. 62, II","tip":"Alistamento ou transferência eleitoral = 2 dias."},
    {"cat":"Faltas","q":"A doação de sangue garante ao servidor 2 dias de ausência justificada por ano.","g":"E","art":"Art. 62, I","tip":"Doação de sangue = 1 dia (não 2)."},
    # LICENÇAS
    {"cat":"Licenças","q":"A licença-maternidade tem duração de 180 dias.","g":"C","art":"Art. 149-A","tip":"Licença-maternidade = 180 dias, antecipável em 28 dias."},
    {"cat":"Licenças","q":"A licença-paternidade tem duração de 10 dias úteis.","g":"E","art":"Art. 150","tip":"Licença-paternidade = 7 dias CONSECUTIVOS."},
    {"cat":"Licenças","q":"A licença por doença em familiar pode ser concedida com remuneração por até 180 dias por ano.","g":"C","art":"Art. 134, §3º","tip":"Máximo 180 dias/ano com remuneração."},
    {"cat":"Licenças","q":"A licença para acompanhar cônjuge deslocado pode durar até 5 anos, sem remuneração.","g":"C","art":"Art. 133, §1º","tip":"Até 5 anos, sem remuneração."},
    {"cat":"Licenças","q":"A licença para tratar de interesses particulares pode durar até 3 anos, prorrogável por mais 3 anos.","g":"C","art":"Art. 144","tip":"3 + 3 anos, sem remuneração."},
    {"cat":"Licenças","q":"A licença-servidor (licença-prêmio) é devida a cada 10 anos de efetivo exercício.","g":"E","art":"Art. 139","tip":"Licença-servidor = a cada 5 anos (quinquênio)."},
    {"cat":"Licenças","q":"A licença-servidor tem duração de 3 meses com remuneração integral.","g":"C","art":"Art. 139","tip":"3 meses a cada 5 anos."},
    {"cat":"Licenças","q":"A gestante comissionada não pode ser exonerada de ofício até 5 meses após o parto.","g":"C","art":"Art. 53","tip":"Proteção = 5 meses após o parto, inclusive para CC."},
    {"cat":"Licenças","q":"A licença para atividade política é concedida com remuneração desde a convenção partidária.","g":"E","art":"Art. 137","tip":"COM remuneração: do REGISTRO até 10 dias após eleição. SEM: da convenção até véspera do registro."},
    # ACUMULAÇÃO
    {"cat":"Acumulação","q":"É permitida a acumulação de dois cargos de professor com compatibilidade de horários.","g":"C","art":"Art. 47, I","tip":"Acumulação permitida: 2 professores, professor+técnico/científico, 2 saúde."},
    {"cat":"Acumulação","q":"O prazo para apresentar opção na acumulação ilegal é de 10 dias improrrogáveis.","g":"C","art":"Art. 48","tip":"10 dias improrrogáveis da ciência da notificação."},
    {"cat":"Acumulação","q":"A proibição de acumular cargos não se aplica às empresas públicas e sociedades de economia mista.","g":"E","art":"Art. 47, §único","tip":"A vedação se estende a toda a Administração Indireta, incluindo empresas públicas e SEM."},
    {"cat":"Acumulação","q":"O servidor investido em mandato de vereador pode acumular os vencimentos de ambos se houver compatibilidade de horários.","g":"C","art":"Art. 55, II","tip":"Única hipótese de acumulação remuneratória com mandato eletivo."},
    # PETIÇÃO
    {"cat":"Petição","q":"O prazo para interpor recurso ou pedido de reconsideração é de 30 dias.","g":"C","art":"Art. 172","tip":"Recurso e reconsideração = 30 dias."},
    {"cat":"Petição","q":"O direito de requerer prescreve em 5 anos nos casos relativos a demissão e interesse patrimonial.","g":"C","art":"Art. 175, I e II","tip":"5 anos: demissão, cassação e interesse patrimonial."},
    {"cat":"Petição","q":"Nos demais casos, o direito de requerer prescreve em 60 dias.","g":"E","art":"Art. 175, III","tip":"Demais casos = 120 dias (não 60)."},
    # PROCESSO DISCIPLINAR
    {"cat":"Disciplinar","q":"O registro da advertência é cancelado após 3 anos sem nova infração.","g":"C","art":"Art. 201","tip":"Advertência: 3 anos. Suspensão: 5 anos."},
    {"cat":"Disciplinar","q":"O registro da suspensão é cancelado após 5 anos sem nova infração.","g":"C","art":"Art. 201","tip":"Suspensão: 5 anos. Advertência: 3 anos."},
    {"cat":"Disciplinar","q":"A ação disciplinar para demissão prescreve em 5 anos.","g":"C","art":"Art. 208, I","tip":"Demissão = 5 anos. Suspensão = 2 anos. Advertência = 1 ano."},
    {"cat":"Disciplinar","q":"A ação disciplinar para suspensão prescreve em 3 anos.","g":"E","art":"Art. 208, II","tip":"Suspensão prescreve em 2 anos (não 3)."},
    {"cat":"Disciplinar","q":"A ação disciplinar para advertência prescreve em 1 ano.","g":"C","art":"Art. 208, III","tip":"Advertência = 1 ano."},
    {"cat":"Disciplinar","q":"O prazo para conclusão da sindicância é de 30 dias, prorrogável por mais 30.","g":"C","art":"Art. 214, §2º","tip":"Sindicância: 30 + 30 dias."},
    {"cat":"Disciplinar","q":"O prazo para conclusão do PAD é de 60 dias, prorrogável por mais 60.","g":"C","art":"Art. 217, §1º","tip":"PAD: 60 + 60 dias."},
    {"cat":"Disciplinar","q":"O afastamento preventivo pode durar até 60 dias improrrogáveis.","g":"E","art":"Art. 222","tip":"Afastamento preventivo: 60 + 60 dias (prorrogável), sem prejuízo de remuneração."},
    {"cat":"Disciplinar","q":"O prazo para defesa escrita no PAD com 1 acusado é de 10 dias.","g":"C","art":"Art. 250","tip":"1 acusado: 10 dias. 2+ acusados: 20 dias."},
    {"cat":"Disciplinar","q":"O prazo para defesa escrita no PAD com 2 ou mais acusados é de 20 dias.","g":"C","art":"Art. 250","tip":"2+ acusados: 20 dias. Prorrogável pelo dobro."},
    {"cat":"Disciplinar","q":"O julgamento do PAD deve ser proferido em 20 dias do recebimento dos autos.","g":"C","art":"Art. 256","tip":"Julgamento: 20 dias dos autos recebidos."},
    {"cat":"Disciplinar","q":"A revisão do processo disciplinar pode resultar em agravamento da penalidade.","g":"E","art":"Art. 270","tip":"Revisão: vedada a reformatio in pejus."},
    {"cat":"Disciplinar","q":"A absolvição criminal por insuficiência de provas afasta a responsabilidade administrativa.","g":"E","art":"Art. 184","tip":"Só afasta se reconhecida inexistência do fato ou negada a autoria."},
    # REMUNERAÇÃO
    {"cat":"Remuneração","q":"O adicional de insalubridade no grau máximo é de 40% sobre o vencimento básico.","g":"C","art":"Art. 88","tip":"Mínimo: 10%, Médio: 20%, Máximo: 40%."},
    {"cat":"Remuneração","q":"O adicional de periculosidade é de 25% sobre o vencimento básico.","g":"E","art":"Art. 89","tip":"Periculosidade = 30% (não 25%). 25% é o noturno."},
    {"cat":"Remuneração","q":"Os adicionais de insalubridade e periculosidade podem ser acumulados quando o servidor exercer atividades que justifiquem ambos.","g":"E","art":"Art. 88, §2º","tip":"NÃO são cumuláveis. O servidor opta pelo mais favorável."},
    {"cat":"Remuneração","q":"A hora noturna, entre 22h e 5h, equivale a 52 minutos e 30 segundos.","g":"C","art":"Art. 85, §2º","tip":"Hora noturna = 52min30s (menor que a hora normal de 60min)."},
    # INFRAÇÕES LEVES — ADVERTÊNCIA (Art. 190)
    {"cat":"Infração Leve","q":"Retirar da repartição qualquer documento ou objeto sem anuência da chefia é infração punível com advertência.","g":"C","art":"Art. 190, II","tip":"Infração leve = advertência. Reincidência: suspensão de até 30 dias."},
    {"cat":"Infração Leve","q":"Recusar-se a participar de programa de treinamento obrigatório constitui infração punível com suspensão.","g":"E","art":"Art. 190, VII","tip":"É infração LEVE → advertência (não suspensão)."},
    {"cat":"Infração Leve","q":"Negar fé a documento público é infração punível com advertência.","g":"C","art":"Art. 190, VI","tip":"Infração leve. Reincidência eleva para suspensão de até 30 dias."},
    {"cat":"Infração Leve","q":"O servidor que não comparece a inspeção ou perícia médica quando convocado pratica infração leve, punível com advertência.","g":"C","art":"Art. 190, VIII","tip":"Ausência a inspeção médica = infração leve → advertência."},
    {"cat":"Infração Leve","q":"Cometer a outro servidor atribuições estranhas ao seu cargo, fora de emergência, é infração punível com demissão.","g":"E","art":"Art. 190, X","tip":"É infração LEVE → advertência, não demissão."},
    {"cat":"Infração Leve","q":"Opor resistência injustificada ao andamento de processo ou serviço é infração punível com advertência.","g":"C","art":"Art. 190, IX","tip":"Infração leve. Reincidência: suspensão de até 30 dias."},
    {"cat":"Infração Leve","q":"Usar indevidamente a identificação funcional em benefício próprio ou de terceiros é infração leve.","g":"C","art":"Art. 190, XV","tip":"Carteira/crachá funcional indevidamente usado = advertência."},
    {"cat":"Infração Leve","q":"Descumprir decisões administrativas regularmente emitidas pela chefia é infração punível com suspensão de até 90 dias.","g":"E","art":"Art. 190, I","tip":"É infração LEVE → advertência. Suspensão de 90 dias corresponde ao Grupo II."},
    # INFRAÇÕES MÉDIAS — SUSPENSÃO ATÉ 30 DIAS (Art. 191)
    {"cat":"Infração Média","q":"Exercer atividade privada durante o expediente de trabalho sujeita o servidor a suspensão de até 30 dias.","g":"C","art":"Art. 191, III","tip":"Atividade privada NO horário de serviço = suspensão até 30 dias (Grupo I)."},
    {"cat":"Infração Média","q":"Praticar comércio ou usura dentro da repartição é punido com advertência.","g":"E","art":"Art. 191, V","tip":"Comércio/usura na repartição = suspensão de até 30 dias (não advertência)."},
    {"cat":"Infração Média","q":"Discriminar subordinado no trabalho por motivo de raça, sexo ou idade é infração punível com suspensão de até 30 dias.","g":"C","art":"Art. 191, VI","tip":"Discriminação no ambiente de trabalho = suspensão até 30 dias (Grupo I)."},
    {"cat":"Infração Média","q":"Praticar ato incompatível com a moralidade administrativa implica suspensão de até 30 dias.","g":"C","art":"Art. 191, IV","tip":"Ato imoral = suspensão até 30 dias."},
    {"cat":"Infração Média","q":"Cometer a pessoa estranha à repartição atribuições de servidor ou subordinado sujeita à suspensão de até 30 dias.","g":"C","art":"Art. 191, I","tip":"Terceiro estranho exercendo função pública = suspensão até 30 dias."},
    # INFRAÇÕES MÉDIAS — SUSPENSÃO ATÉ 90 DIAS (Art. 192)
    {"cat":"Infração Média","q":"O assédio moral ou sexual praticado por servidor é punido com suspensão de até 90 dias.","g":"C","art":"Art. 192, II","tip":"Assédio = suspensão até 90 dias (Grupo II)."},
    {"cat":"Infração Média","q":"A ofensa física em serviço sujeita o servidor a suspensão de até 90 dias, inclusive quando praticada em legítima defesa.","g":"E","art":"Art. 192, I","tip":"Legítima defesa própria é EXCEÇÃO: não configura a infração."},
    {"cat":"Infração Média","q":"Fornecer senha de acesso a sistema para pessoa não autorizada sujeita o servidor a suspensão de até 90 dias.","g":"C","art":"Art. 192, VI","tip":"Facilitar acesso restrito a não autorizado = suspensão até 90 dias."},
    {"cat":"Infração Média","q":"Exercer atividade privada incompatível com o cargo, mesmo fora do horário de expediente, é punido com suspensão de até 90 dias.","g":"C","art":"Art. 192, IV","tip":"Incompatibilidade fora do expediente = 90 dias (mais grave que dentro = 30 dias)."},
    {"cat":"Infração Média","q":"Coagir subordinado a filiar-se a sindicato ou partido político sujeita à suspensão de até 90 dias.","g":"C","art":"Art. 192, III","tip":"Coação sindical/partidária = suspensão até 90 dias (Grupo II)."},
    {"cat":"Infração Média","q":"Usar recursos computacionais da repartição para disseminar vírus ou acessar sites remunerados é punido com advertência.","g":"E","art":"Art. 192, V","tip":"Mau uso de TI = suspensão até 90 dias (não advertência)."},
    # INFRAÇÕES GRAVES — DEMISSÃO GRUPO I (Art. 193)
    {"cat":"Infração Grave","q":"O abandono de cargo por mais de 30 dias consecutivos resulta em demissão.","g":"C","art":"Art. 193, I c/c Art. 64, I","tip":"Abandono (30 dias) e inassiduidade (60 dias interpolados) = demissão (Grupo I)."},
    {"cat":"Infração Grave","q":"Proceder de forma desidiosa, com negligência reiterada nos deveres, é infração grave punível com demissão.","g":"C","art":"Art. 193, III","tip":"Desídia = demissão (Grupo I). Não gera impedimento de 10 anos."},
    {"cat":"Infração Grave","q":"Aceitar comissão, emprego ou pensão de Estado estrangeiro é infração punível com demissão.","g":"C","art":"Art. 193, VIII","tip":"Vínculo com Estado estrangeiro = demissão (Grupo I)."},
    {"cat":"Infração Grave","q":"A acumulação ilegal de cargos públicos é infração punível com suspensão de até 90 dias.","g":"E","art":"Art. 193, II","tip":"Acumulação ilegal = DEMISSÃO (Grupo I), não suspensão."},
    {"cat":"Infração Grave","q":"Insubordinação grave que subverte ostensivamente a ordem hierárquica é punida com demissão.","g":"C","art":"Art. 193, V","tip":"Insubordinação grave = demissão (Grupo I)."},
    {"cat":"Infração Grave","q":"Dispensar licitação de forma ilegal para contratar empresa de parente configura infração grave punível com demissão.","g":"C","art":"Art. 193, VI","tip":"Dispensa ilegal de licitação = demissão (Grupo I)."},
    # INFRAÇÕES GRAVES — DEMISSÃO GRUPO II (Art. 194) — 10 ANOS DE IMPEDIMENTO
    {"cat":"Infração Grave","q":"A demissão por improbidade administrativa impede o ex-servidor de assumir cargo no DF por 10 anos.","g":"C","art":"Art. 194, I","tip":"Grupo II = demissão + impedimento de 10 anos para novo cargo no DF."},
    {"cat":"Infração Grave","q":"A demissão por abandono de cargo impede o servidor de retornar ao serviço público do DF por 10 anos.","g":"E","art":"Art. 193 x Art. 194","tip":"Abandono é Grupo I (Art. 193): SEM impedimento de 10 anos. Só o Grupo II (Art. 194) gera o impedimento."},
    {"cat":"Infração Grave","q":"Exigir, solicitar ou aceitar propina ou presente de pessoa com interesse em decisão administrativa resulta em demissão.","g":"C","art":"Art. 194, III","tip":"Corrupção passiva = demissão (Grupo II) + 10 anos de impedimento."},
    {"cat":"Infração Grave","q":"Usar conhecimentos do cargo para invadir sistemas da repartição é infração grave do Grupo II.","g":"C","art":"Art. 194, II","tip":"Ataque a sistemas usando saberes do cargo = Grupo II: demissão + 10 anos."},
    {"cat":"Infração Grave","q":"Valer-se do cargo para obter proveito indevido para si ou terceiros é infração do Grupo I, punível com demissão simples.","g":"E","art":"Art. 194, IV","tip":"Valer-se do cargo para proveito indevido = Grupo II (Art. 194): demissão + 10 anos de impedimento."},
    # DEVERES (Art. 43)
    {"cat":"Deveres","q":"O servidor deve cumprir as ordens dos superiores hierárquicos, mesmo quando manifestamente ilegais.","g":"E","art":"Art. 43, IV","tip":"Dever de obediência com RESSALVA: não se aplica a ordens manifestamente ilegais."},
    {"cat":"Deveres","q":"É dever do servidor comunicar à autoridade superior qualquer irregularidade de que tenha ciência no exercício do cargo.","g":"C","art":"Art. 43, VI","tip":"Denunciar irregularidades é dever funcional, não mera faculdade."},
    {"cat":"Deveres","q":"Tratar com urbanidade as pessoas é dever funcional do servidor público.","g":"C","art":"Art. 43, XI","tip":"Urbanidade = dever expresso no Art. 43. Violação = infração disciplinar."},
    {"cat":"Deveres","q":"Ser assíduo e pontual ao serviço é dever do servidor, podendo seu descumprimento ensejar infração disciplinar.","g":"C","art":"Art. 43, X","tip":"Assiduidade e pontualidade constam expressamente no rol de deveres."},
    {"cat":"Deveres","q":"O dever de guardar sigilo sobre assuntos da repartição pode ser afastado por ordem do superior imediato.","g":"E","art":"Art. 43, VIII","tip":"Sigilo é dever irrestrito. Nenhum superior tem poder de dispensar o servidor desse dever."},
    {"cat":"Deveres","q":"Zelar pela economia do material e pela conservação do patrimônio público é dever funcional expresso na LC 840.","g":"C","art":"Art. 43, VII","tip":"Conservação do patrimônio público é dever de todos os servidores."},
    {"cat":"Deveres","q":"Manter conduta compatível com a moralidade administrativa é dever do servidor, não apenas uma recomendação ética.","g":"C","art":"Art. 43, IX","tip":"Moralidade administrativa = dever legal expresso, não mera diretriz."},
    # RESPONSABILIDADE (Art. 183-184)
    {"cat":"Responsabilidade","q":"As responsabilidades civil, penal e administrativa do servidor são independentes entre si.","g":"C","art":"Art. 184","tip":"Independência das três esferas: prazos, provas e decisões são autônomas."},
    {"cat":"Responsabilidade","q":"A absolvição criminal por insuficiência de provas impede a punição administrativa pelo mesmo fato.","g":"E","art":"Art. 184","tip":"Só vincula se houver reconhecimento de INEXISTÊNCIA DO FATO ou NEGATIVA DE AUTORIA."},
    {"cat":"Responsabilidade","q":"A decisão judicial que reconhece a inexistência material do fato vincula obrigatoriamente a esfera administrativa.","g":"C","art":"Art. 184","tip":"Inexistência do fato e negação de autoria na esfera penal vinculam as demais esferas."},
    {"cat":"Responsabilidade","q":"A condenação criminal do servidor implica automaticamente sua demissão do cargo público.","g":"E","art":"Art. 184","tip":"Independência das esferas: condenação penal não gera demissão automática — depende de PAD."},
    {"cat":"Responsabilidade","q":"O servidor responde civil, penal e administrativamente pelo exercício irregular de suas atribuições.","g":"C","art":"Art. 183","tip":"Responsabilidade tríplice pelo exercício irregular do cargo."},
    # PROIBIÇÕES (Art. 44)
    {"cat":"Proibições","q":"É vedado ao servidor atuar como procurador ou intermediário de interesses privados junto à Administração Pública do DF.","g":"C","art":"Art. 44","tip":"Proibição absoluta: nepotismo e intermediação de interesses são incompatíveis com o cargo."},
    {"cat":"Proibições","q":"É proibido ao servidor receber propina, comissão ou presente em razão das atribuições de seu cargo.","g":"C","art":"Art. 44","tip":"Vedação absoluta. Constitui infração grave (Art. 194, III) com demissão + 10 anos de impedimento."},
    {"cat":"Proibições","q":"A proibição de praticar usura restringe-se ao horário de expediente e ao ambiente da repartição.","g":"E","art":"Art. 44","tip":"Proibição de usura é ABSOLUTA: independe de local ou horário."},
    {"cat":"Proibições","q":"É vedado ao servidor participar de gerência ou administração de sociedade privada, salvo exceções previstas em lei.","g":"C","art":"Art. 44","tip":"Participação em gerência privada é proibida, ressalvadas as hipóteses legais (acionista, cotista etc.)."},
    {"cat":"Proibições","q":"O servidor pode exercer qualquer atividade privada fora do expediente, desde que não prejudique o desempenho do cargo.","g":"E","art":"Art. 44 c/c Art. 192, IV","tip":"Atividade privada INCOMPATÍVEL com o cargo é vedada mesmo fora do expediente."},
    # CARGO EM COMISSÃO E FUNÇÃO DE CONFIANÇA
    {"cat":"Provimento","q":"As funções de confiança só podem ser exercidas por servidores ocupantes de cargo efetivo.","g":"C","art":"Art. 9º, §1º","tip":"FC = exclusiva para efetivos. CC pode ser qualquer pessoa (livre nomeação)."},
    {"cat":"Provimento","q":"O servidor efetivo nomeado para cargo em comissão perde automaticamente seu cargo efetivo.","g":"E","art":"Art. 11","tip":"O cargo efetivo fica resguardado: o servidor pode retornar a ele quando deixar o CC."},
    {"cat":"Provimento","q":"O cargo em comissão pode ser exonerado a qualquer tempo, independentemente de motivação.","g":"C","art":"Art. 8º","tip":"CC = livre nomeação e exoneração (ad nutum). Diferente do efetivo, que exige processo."},
    {"cat":"Provimento","q":"Ao menos 70% dos cargos em comissão do DF devem ser ocupados por servidores de carreira.","g":"C","art":"Art. 10, §1º","tip":"70% CC para efetivos. A questão com 50% é a mais cobrada como pegadinha."},
    # REMUNERAÇÃO — QUINQUÊNIO
    {"cat":"Remuneração","q":"O adicional por tempo de serviço (quinquênio) corresponde a 5% do vencimento básico a cada 5 anos.","g":"C","art":"Art. 82","tip":"Quinquênio = 5% por período de 5 anos de efetivo exercício."},
    {"cat":"Remuneração","q":"O adicional por tempo de serviço pode ultrapassar 35% do vencimento básico com o acúmulo de quinquênios.","g":"E","art":"Art. 82","tip":"Limite máximo = 7 quinquênios = 35% do vencimento básico."},
    {"cat":"Remuneração","q":"O adicional por tempo de serviço incide sobre a remuneração total do servidor, incluindo gratificações.","g":"E","art":"Art. 82","tip":"Quinquênio incide sobre o VENCIMENTO BÁSICO, não sobre a remuneração total."},
]

CATS = sorted(set(q["cat"] for q in QUESTOES))

CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: #0d1117; color: #e6edf3; font-family: 'Segoe UI', sans-serif; min-height: 100vh; display: flex; flex-direction: column; align-items: center; padding: 20px; }
h1 { font-size: 1.4rem; color: #f85149; margin-bottom: 4px; }
.sub { color: #8b949e; font-size: .85rem; margin-bottom: 16px; text-align: center; }
.controls { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 14px; justify-content: center; }
.controls label { background: #161b22; border: 1px solid #30363d; border-radius: 6px; padding: 5px 10px; font-size: .78rem; cursor: pointer; display: flex; align-items: center; gap: 5px; }
.controls label:hover { border-color: #f85149; }
.controls input[type=checkbox] { accent-color: #f85149; }
.btn-start { background: #b62324; color: #fff; border: none; border-radius: 8px; padding: 10px 28px; font-size: 1rem; cursor: pointer; }
.btn-start:hover { background: #f85149; }
#game { display: none; width: 100%; max-width: 640px; }
.score-bar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; font-size: .88rem; color: #8b949e; }
#num-badge { background: #161b22; border: 1px solid #30363d; border-radius: 6px; padding: 4px 10px; font-size: .8rem; }
.timer-wrap { height: 8px; background: #21262d; border-radius: 4px; margin-bottom: 16px; overflow: hidden; }
#timer-bar { height: 8px; border-radius: 4px; background: #f85149; transition: width 1s linear; }
.card { background: #161b22; border: 2px solid #30363d; border-radius: 12px; padding: 24px 22px; margin-bottom: 16px; transition: border-color .15s, background .15s; }
.card.flash-ok { border-color: #3fb950; background: rgba(63,185,80,.15); }
.card.flash-nok { border-color: #f85149; background: rgba(248,81,73,.15); }
.cat-tag { font-size: .72rem; color: #8b949e; text-transform: uppercase; letter-spacing: .5px; margin-bottom: 8px; }
.question { font-size: 1.05rem; line-height: 1.6; }
.btns { display: flex; gap: 12px; margin-top: 18px; }
.btn-ce { flex: 1; padding: 16px; border: 2px solid; border-radius: 10px; font-size: 1.1rem; font-weight: 700; cursor: pointer; transition: .1s; background: transparent; }
.btn-ce.certo { border-color: #3fb950; color: #3fb950; }
.btn-ce.certo:hover { background: rgba(63,185,80,.2); }
.btn-ce.errado { border-color: #f85149; color: #f85149; }
.btn-ce.errado:hover { background: rgba(248,81,73,.2); }
.kbd { font-size: .65rem; display: block; color: #484f58; margin-top: 4px; }
#result { display: none; width: 100%; max-width: 640px; }
.result-header { text-align: center; padding: 20px; }
.result-header h2 { font-size: 1.6rem; margin-bottom: 6px; }
.score-big { font-size: 3rem; font-weight: 700; color: #f85149; margin: 8px 0; }
.score-label { color: #8b949e; margin-bottom: 16px; }
.erros-titulo { font-size: .85rem; text-transform: uppercase; letter-spacing: .5px; color: #8b949e; margin-bottom: 10px; padding: 0 4px; }
.erro-item { background: #161b22; border-left: 3px solid #f85149; border-radius: 0 8px 8px 0; padding: 12px 14px; margin-bottom: 8px; }
.erro-q { font-size: .9rem; margin-bottom: 6px; }
.erro-meta { display: flex; gap: 10px; flex-wrap: wrap; font-size: .78rem; }
.gabarito { padding: 2px 8px; border-radius: 10px; font-weight: 700; }
.gabarito.C { background: rgba(63,185,80,.15); color: #3fb950; border: 1px solid #3fb950; }
.gabarito.E { background: rgba(248,81,73,.15); color: #f85149; border: 1px solid #f85149; }
.art-txt { color: #8b949e; }
.tip-txt { color: #c9d1d9; flex-basis: 100%; margin-top: 4px; }
.btn-retry { background: #b62324; color: #fff; border: none; border-radius: 8px; padding: 12px 28px; font-size: .95rem; cursor: pointer; margin: 16px auto; display: block; }
.btn-retry:hover { background: #f85149; }
.feedback { display: none; margin-top: 16px; padding-top: 14px; border-top: 1px solid #30363d; }
.fb-result { font-size: 1.1rem; font-weight: 700; margin-bottom: 8px; }
.fb-result.ok { color: #3fb950; }
.fb-result.nok { color: #f85149; }
.fb-gabarito { margin-bottom: 8px; font-size: .88rem; }
.fb-art { color: #8b949e; font-size: .8rem; margin-bottom: 5px; }
.fb-tip { color: #c9d1d9; font-size: .9rem; line-height: 1.55; }
#btn-proxima { display: none; width: 100%; max-width: 640px; margin-top: 10px; background: #1f6feb; color: #fff; border: none; border-radius: 8px; padding: 14px; font-size: 1rem; font-weight: 700; cursor: pointer; }
#btn-proxima:hover { background: #388bfd; }
"""

JS = r"""
const QUESTOES = __QUESTOES__;
let deck=[], idx=0, acertos=0, erros=[], timer=null, secs=5, esperando=false;

function shuffle(a){for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;}
function getSelected(){return [...document.querySelectorAll('.controls input:checked')].map(i=>i.value);}

function startGame(){
  const sel=getSelected();
  deck=shuffle(QUESTOES.filter(q=>sel.includes(q.cat)));
  if(!deck.length){alert('Selecione ao menos uma categoria!');return;}
  idx=0;acertos=0;erros=[];esperando=false;
  document.getElementById('setup').style.display='none';
  document.getElementById('game').style.display='block';
  document.getElementById('result').style.display='none';
  document.addEventListener('keydown', onKey);
  nextQ();
}

function onKey(e){
  if(esperando){ if(e.key==='Enter'||e.key===' ') proxima(); return; }
  if(e.key==='c'||e.key==='C') responder('C');
  if(e.key==='e'||e.key==='E') responder('E');
}

function nextQ(){
  if(idx>=deck.length){showResult();return;}
  esperando=false;
  const q=deck[idx];
  document.getElementById('num-badge').textContent=`${idx+1} / ${deck.length}`;
  document.getElementById('score-val').textContent=acertos;
  document.querySelector('.cat-tag').textContent=q.cat;
  document.querySelector('.question').textContent=q.q;
  const card=document.querySelector('.card');
  card.className='card';
  startTimer();
}

function startTimer(){
  clearInterval(timer);
  secs=5;
  const bar=document.getElementById('timer-bar');
  bar.style.transition='none';
  bar.style.width='100%';
  setTimeout(()=>{ bar.style.transition='width 1s linear'; bar.style.width='0%'; },30);
  timer=setInterval(()=>{
    secs--;
    if(secs<=0){clearInterval(timer);timeout();}
  },1000);
}

function timeout(){
  const q=deck[idx];
  erros.push(q);
  flash(false);
}

function responder(resp){
  if(esperando) return;
  clearInterval(timer);
  const q=deck[idx];
  const ok=(resp===q.g);
  if(ok) acertos++; else erros.push(q);
  flash(ok);
}

function flash(ok){
  esperando=true;
  const card=document.querySelector('.card');
  card.classList.add(ok?'flash-ok':'flash-nok');
  const q=deck[idx];
  const fb=document.getElementById('feedback');
  fb.innerHTML=`<div class="fb-result ${ok?'ok':'nok'}">${ok?'✓ Correto!':'✗ Errado!'}</div>`+
    `<div class="fb-gabarito">Gabarito: <span class="gabarito ${q.g}">${q.g==='C'?'CERTO':'ERRADO'}</span></div>`+
    `<div class="fb-art">${q.art}</div>`+
    `<div class="fb-tip">${q.tip}</div>`;
  fb.style.display='block';
  document.getElementById('btn-proxima').style.display='block';
}

function proxima(){
  document.getElementById('feedback').style.display='none';
  document.getElementById('btn-proxima').style.display='none';
  idx++;
  nextQ();
}

function showResult(){
  document.removeEventListener('keydown', onKey);
  document.getElementById('game').style.display='none';
  const res=document.getElementById('result');
  res.style.display='block';
  const total=deck.length, pct=Math.round(acertos/total*100);
  res.querySelector('h2').textContent=pct>=80?'Reflexos afiados! ⚡':pct>=60?'Bom ritmo! 💪':'Precisa de mais treino! 📚';
  res.querySelector('.score-big').textContent=`${acertos}/${total}`;
  res.querySelector('.score-label').textContent=`${pct}% de acerto • ${erros.length} erros`;
  const lista=document.getElementById('lista-erros');
  lista.innerHTML='';
  if(erros.length===0){
    lista.innerHTML='<p style="color:#3fb950;text-align:center;padding:16px">Perfeito! Nenhum erro! 🎯</p>';
  } else {
    erros.forEach(q=>{
      const d=document.createElement('div');
      d.className='erro-item';
      d.innerHTML=`<div class="erro-q">${q.q}</div>
        <div class="erro-meta">
          <span class="gabarito ${q.g}">${q.g==='C'?'CERTO':'ERRADO'}</span>
          <span class="art-txt">${q.art}</span>
          <span class="tip-txt">${q.tip}</span>
        </div>`;
      lista.appendChild(d);
    });
  }
}

function retryAll(){
  document.getElementById('result').style.display='none';
  document.getElementById('setup').style.display='block';
}
"""

def build_html():
    import json
    cats_checkboxes = "\n    ".join(
        f'<label><input type="checkbox" value="{c}" checked> {c}</label>'
        for c in CATS
    )
    js = JS.replace("__QUESTOES__", json.dumps(QUESTOES, ensure_ascii=False))
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Speed Round — LC 840/2011</title>
<style>{CSS}</style>
</head>
<body>
<h1>⚡ Speed Round</h1>
<p class="sub">LC 840/2011 — {len(QUESTOES)} questões • 5 segundos por questão • Teclas C / E</p>
<div id="setup" style="width:100%;max-width:640px">
  <p style="color:#8b949e;font-size:.82rem;margin-bottom:8px;text-align:center">Categorias:</p>
  <div class="controls">{cats_checkboxes}</div>
  <div style="text-align:center"><button class="btn-start" onclick="startGame()">⚡ Iniciar</button></div>
</div>
<div id="game">
  <div class="score-bar">
    <span>Acertos: <span id="score-val" style="color:#3fb950">0</span></span>
    <span id="num-badge">1/{len(QUESTOES)}</span>
  </div>
  <div class="timer-wrap"><div id="timer-bar" style="width:100%"></div></div>
  <div class="card">
    <div class="cat-tag"></div>
    <div class="question"></div>
    <div class="btns">
      <button class="btn-ce certo" onclick="responder('C')">✓ CERTO<span class="kbd">tecla C</span></button>
      <button class="btn-ce errado" onclick="responder('E')">✗ ERRADO<span class="kbd">tecla E</span></button>
    </div>
    <div id="feedback" class="feedback"></div>
  </div>
  <button id="btn-proxima" onclick="proxima()">Próxima → <span style="font-size:.72rem;font-weight:400;opacity:.65">Enter / Espaço</span></button>
</div>
<div id="result">
  <div class="result-header">
    <h2></h2>
    <div class="score-big"></div>
    <div class="score-label"></div>
  </div>
  <p class="erros-titulo">Questões erradas:</p>
  <div id="lista-erros"></div>
  <button class="btn-retry" onclick="retryAll()">↩ Jogar novamente</button>
</div>
<script>{js}</script>
</body>
</html>"""

html = build_html()
with open(r"c:\Users\hacke\OneDrive - unb.br\estudo\speed_lc840.html","w",encoding="utf-8") as f:
    f.write(html)
print(f"Criado! speed_lc840.html — {len(QUESTOES)} questões, {len(html)//1024}KB")
