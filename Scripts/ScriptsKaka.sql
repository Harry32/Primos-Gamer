CREATE TABLE Produtos(
	id INT iIDENTITY,
	nome VARCHAR(50) NOT NULL,
	fabricante VARCHAR(100) NOT NULL,
	modelo VARCHAR(100),
	preco NUMERIC(16,2) NOT NULL,
	descricao VARCHAR(500),
	data_cadastro TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
	especificacoes VARCHAR(300),
	ativo BOOL NOT NULL
);
/
INSERT INTO Produtos(id, nome, fabricante, modelo, preco, descricao, especificacoes, ativo)
VALUES (
  1,
  'Notebook Gamer Dell G5',
  'Dell',
  'G5-5590-A30B',
  7299.99,
  'O Dell G5 oferece uma experiência de jogo fluida e gráficos de     alta qualidade.',
  'Processador: Intel Core i7-9750H, Memória: 16GB DDR4,   Armazenamento: 1TB HDD + 256GB SSD, Placa de Vídeo: NVIDIA  GeForce GTX 1660 Ti, Tela: 15.6 polegadas Full HD, Peso: 2.68kg',
  1
);

INSERT INTO Produtos(id, nome, fabricante, modelo, preco, descricao, especificacoes, ativo)
VALUES (
  2,
  'Notebook Gamer Lenovo Legion Y540',
  'Lenovo',
  'Legion Y540-15IRH',
  6999.99,
  'O Lenovo Legion Y540 é um notebook gamer de alta performance com design elegante.',
  'Processador: Intel Core i7-9750H, Memória: 16GB DDR4, Armazenamento: 512GB SSD, Placa de    Vídeo: NVIDIA GeForce GTX 1660 Ti, Tela: 15.6 polegadas Full HD, Peso: 2.3kg',
  1
);

INSERT INTO Produtos(id, nome, fabricante, modelo, preco, descricao, especificacoes, ativo)
VALUES (
  3,
  'Notebook Gamer ASUS TUF A15',
  'ASUS',
  'TUF A15 FA506IV',
  7499.99,
  'O ASUS TUF Gaming A15 combina durabilidade militar com um desempenho excelente para jogos.',
  'Processador: AMD Ryzen 7 4800H, Memória: 16GB DDR4, Armazenamento: 512GB SSD, Placa de Vídeo: NVIDIA GeForce RTX 2060, Tela: 15.6 polegadas Full HD 144Hz, Peso: 2.3kg',
  1
);

INSERT INTO Produtos(id, nome, fabricante, modelo, preco, descricao, especificacoes, ativo)
VALUES (
  4,
  'Processador AMD Ryzen 7 5700X3D',
  'AMD',
  '100-100001503WOF',
  2499.99,
  'Desfrute de velocidades supersônicas com 8 núcleos e 16 threads de processamento, prontos para enfrentar os títulos mais desafiadores. Frequência base de 3,0GHz e boost dinâmico de até 4,1GHz para eliminar qualquer engasgo.',
  'Nº de núcleos de CPU: 8, Nº de threds: 16, Clock de max boost: 4.1, Soquete: AM4, Peso: 243g',
  1
);

INSERT INTO Produtos(id, nome, fabricante, modelo, preco, descricao, especificacoes, ativo)
VALUES (
  5,
  'Processador Intel Core i9-13900K',
  'Intel',
  'BX8071513900K',
  3899.99,
  'O Intel Core i9-13900K é o processador ideal para gamers e profissionais que precisam de desempenho extremo. Equipado com 24 núcleos e 32 threads, alcança frequências de até 5,8 GHz em modo turbo, oferecendo desempenho inigualável.',
  'Nº de núcleos de CPU: 24, Nº de threds: 32, Clock de max boost: 5.8, Soquete: LGA 1700, Peso: 101g',
  1
);

INSERT INTO Produtos(id, nome, fabricante, modelo, preco, descricao, especificacoes, ativo)
VALUES (
  6,
  'Teclado Mecânico Gamer Razer BlackWidow V3',
  'Razer',
  'RZ03-03540100-R3U1',
  999.99,
  'O Razer BlackWidow V3 é equipado com switches mecânicos Razer Green para uma resposta tátil precisa e feedback auditivo satisfatório. Possui iluminação RGB Razer Chroma e estrutura em alumínio para maior durabilidade.',
  'Tipo de Switch: Mecânico, Conectividade: Cabo USB, Iluminação: Razer Chroma RGB, 	   Estrutura: Alumínio, Peso: 1.130kg',
  1
);

INSERT INTO Produtos(id, nome, fabricante, modelo, preco, descricao, especificacoes, ativo)
VALUES (
  7,
  'Teclado Mecânico Gamer Redragon Draconic K530',
  'Redragon',
  'K530-RGB',
  549.99,
  'O Redragon Draconic K530 é um teclado mecânico compacto, sem fio, projetado para máxima portabilidade e desempenho. Equipado com switches Outemu Brown, ideal para quem busca um equilíbrio entre feedback tátil e silêncio, além de conectividade Bluetooth.',
  'Tipo de Switch: Mecânico, Conectividade: Bluetooth 5.0 / Cabo USB-C, Iluminação: RGB, Estrutura: Plástico ABS reforçado, Peso: 600g',
  1
);

INSERT INTO Produtos(id, nome, fabricante, modelo, preco, descricao, especificacoes, ativo)
VALUES (
  8,
  'Mouse Gamer Logitech G403 Hero',
  'Logitech',
  '910-005631',
  399.99,
  'O Logitech G403 Hero é equipado com o sensor HERO 25K, oferecendo precisão máxima com até 25.600 DPI ajustáveis. Design ergonômico, estrutura leve e peso ajustável, ideal para quem busca conforto e alto desempenho em jogos.',
  'DPI Máximo: 25600, Conectividade: Cabo USB, Botões Programáveis: 6, Iluminação: RGB LIGHTSYNC, Tempo de Resposta: 1ms, Peso: 87g',
  1
);

INSERT INTO Produtos(id, nome, fabricante, modelo, preco, descricao, especificacoes, ativo)
VALUES (
  9,
  'Headset Gamer Razer Kraken X',
  'Razer',
  'RZ04-02890100-R3U1',
  299.99,
  'O Razer Kraken X é um headset ultraleve com som surround 7.1 e almofadas em espuma com memória para máximo conforto. Microfone cardioide e estrutura reforçada para durabilidade.',
  'Conectividade: P2 3.5mm, Microfone: Cardioide não removível, Compatibilidade: PC, PS4, Xbox One, Switch, Peso: 250g',
  1
);

INSERT INTO Produtos(id, nome, fabricante, modelo, preco, descricao, especificacoes, ativo)
VALUES (
  10,
  'Headset Gamer Redragon Zeus X',
  'Redragon',
  'H510-RGB',
  329.99,
  'O Readragon Zeus x é um headset que traz um design moderno, qualidade de som surround 7.1, possui almofadas e revestimento interno do arco em tecido para proporcionar o máximo de conforto e  Iluminação RGB Redragon Chroma Mk.II com 4 efeitos.',
  'Conectividade: USB, Microfone: Cardioide não removível, Iluminação RGB Redragon Chroma Mk.II, Compatibilidade: PC, PS4/PS3, Xbox One, Switch e Smartphones, Peso: 810g',
  1
);

INSERT INTO Produtos(id, nome, fabricante, modelo, preco, descricao, especificacoes, ativo)
VALUES (
  11,
  'Placa de Vídeo NVIDIA GeForce RTX 3060 Ventus 2X MSI',
  'MSI',
  'RTX 3060 Ventus',
  2119.99,
  'A RTX 3060 Ventus 2X MSI é equipada com 12GB GDDR6, oferecendo desempenho de última geração para jogos 4K e Ray Tracing. Possui suporte a DLSS e tecnologias avançadas da NVIDIA para máxima performance.',
  'CUDA Cores: 3584, Conectividade: HDMI 2.1, DisplayPort 1.4a, Peso: 1.03 kg',
  1
);

INSERT INTO Produtos(id, nome, fabricante, modelo, preco, descricao, especificacoes, ativo)
VALUES (
  12,
  'Placa de Vídeo AMD Radeon RX 6800 XT',
  'ASRock',
  '90-GA28ZZ-00UANF',
  5799.99,
  'A RX 6800 XT possui 16GB GDDR6 e arquitetura RDNA 2, proporcionando excelente desempenho em jogos 1440p e 4K. Inclui suporte a Ray Tracing e tecnologia Smart Access Memory para CPUs Ryzen.',
  'Stream Processors: 4608, Conectividade: HDMI 2.1, DisplayPort 1.4, Peso: 2.52 kg',
  1
);

INSERT INTO Produtos(id, nome, fabricante, modelo, preco, descricao, especificacoes, ativo)
VALUES (
  13,
  'Placa Mãe ASUS ROG Strix Z590-E',
  'ASUS',
  'ROG STRIX Z590-E GAMING WIFI',
  2999.99,
  'A ROG Strix Z590-E é uma placa-mãe premium para processadores Intel de 11ª geração, com suporte a overclock, Wi-Fi 6E integrado e iluminação RGB ASUS Aura Sync.',
  'Socket: LGA 1200, RAM Suportada: DDR4 até 5333MHz, Peso: 1.2kg',
  1
);

INSERT INTO Produtos(id, nome, fabricante, modelo, preco, descricao, especificacoes, ativo)
VALUES (
  14,
  'Memória RAM Corsair Vengeance RGB Pro 16GB (2x8GB)',
  'Corsair',
  'CMW16GX4M2C3200C16',
  649.99,
  'O kit Corsair Vengeance RGB Pro oferece desempenho de alto nível para jogadores e criadores de conteúdo, com 16GB de capacidade, frequência de 3200MHz e iluminação RGB dinâmica.',
  'Tamanho: 16GB (2x8GB), Frequência: 3200MHz, Compatibilidade: Intel e AMD, Peso: 120g',
  1
);

INSERT INTO Produtos(id, nome, fabricante, modelo, preco, descricao, especificacoes, ativo)
VALUES (
  15,
  'Sony PlayStation 5 Slim',
  'Sony',
  'CFI-1015A',
  3999.99,
  'O PlayStation 5 Slim oferece gráficos de nova geração com suporte a Ray Tracing, tempos de carregamento rápidos com seu SSD customizado e jogos exclusivos que definem a plataforma.',
  'Memoria: 16Gb GDDR6 RAM. CPU: AMD Ryzen Zen 2 8 núcleos. Armazenamento: 1TB SSD Customizado. Peso: 4.05 kg',
  1
);

INSERT INTO Produtos(id, nome, fabricante, modelo, preco, descricao, especificacoes, ativo)
VALUES (
  16,
  'Xbox Series X',
  'Microsoft',
  'XBS-XXA-00001',
  4999.99,
  'O Xbox Series X promete um dos melhores desempenhos já vistos no mundo dos consoles, sendo capaz de rodar jogos com resolução 4K a até 120 frames por segundo, graças a uma GPU da AMD de 12 e com leitor óptico Blu-ray UHD 4K',
  'Memoria: 16Gb GDDR6 RAM. CPU: AMD Zen 2 customizado com 8 núcleos e 16 threads a até 3,8 GHz. Armazenamento: SSD de 1 TB PCIe Gen 4 NVME. Peso: 4.45kg',
  1
);

INSERT INTO Produtos(id, nome, fabricante, modelo, preco, descricao, especificacoes, ativo)
VALUES (
  17,
  'Nintendo Switch',
  'Nintendo',
  'HEG-001',
  2199.99,
  'O Nintendo Switch foi desenvolvido para fazer parte da sua vida, transformando-se de um console doméstico em um console portátil num piscar de olhos. Coloque seu Nintendo Switch na base do console para se divertir jogando em sua televisão. Abra o suporte para compartilhar a tela do seu Nintendo Switch em jogos multijogador. Remova o console da base e jogue com os controles Joy-con encaixados para aproveitar a diversão do seu Nintendo, de onde estiver',
  'Memoria: 4Gb LPDDR4 RAM, CPU: Nvidia Tegra X1 ARM Cortex A57 QuadCore 1.02Ghz. Armazenamento: 64 Gb. Peso: 398g',
  1
);

INSERT INTO Produtos(id, nome, fabricante, modelo, preco, descricao, especificacoes, ativo)
VALUES (
  18,
  'God of War Ragnarök',
  'Sony',
  null,
  349.99,
  'Embarque com Kratos e Atreus em uma jornada épica emocionante sobre apego e superação, viajando pelos Nove Reinos em busca de respostas enquanto as forças asgardianas se preparam para uma batalha profetizada que causará o fim do mundo',
  'Plataformas: PlayStation 5, PlayStation 4, PC. Gêneros: ação e aventura. Classificação: 18 anos',
  1
);

INSERT INTO Produtos(id, nome, fabricante, modelo, preco, descricao, especificacoes, ativo)
VALUES (
  19,
  'Resident Evil 4 Remake',
  'Capcom',
  null,
  199.99,
  'Resident Evil 4, o jogo lendário de terror e sobrevivência de 2005, está totalmente atualizado nesse remake completo. Seis anos após os eventos de Resident Evil 2, Leon Kennedy, sobrevivente de Raccoon City, foi enviado a um vilarejo isolado na Europa para investigar o desaparecimento da filha do presidente dos Estados Unidos.',
  'Plataformas: PlayStation 2, PlayStation 4, Android. Gêneros: Survival horror. Classificação: 18 anos',
  1
);

INSERT INTO Produtos(id, nome, fabricante, modelo, preco, descricao, especificacoes, ativo)
VALUES (
  20,
  'Rayman Legends',
  'Ubysoft',
  null,
  59.99,
  'Rayman, Globox e os Teensies estão vagando por uma floresta encantada quando descobrem uma tenda misteriosa repleta com uma série de pinturas cativantes. Quando olham mais de perto, percebem que cada pintura conta a história de um mundo mítico. O grupo deve correr, pular e lutar ao longo de cada um dos mundos para salvar a pátria e descobrir os segredos de todas as pinturas lendárias',
  'Plataformas: PC, PlayStation 3, PlayStation 4, Wii U, Xbox 360, Xbox One, Switch. Gêneros: Ação e aventura. Classificação: Livre',
  1
);

INSERT INTO Produtos(id, nome, fabricante, modelo, preco, descricao, especificacoes, ativo)
VALUES (
  21,
  'Super Mario Bros. Wonder',
  'Nintendo',
  null,
  299.99,
  'Bem-vindos ao Reino Flor! Mario e seus amigos foram convidados para visitar o colorido Reino Flor, um lugar não muito distante do Reino Cogumelo. Infelizmente, o rei Bowser se transformou em um castelo voador e está criando o caos nestas terras pacíficas. Agora nossos heróis precisam salvar o dia',
  'Plataformas: Nintendo Switch. Gêneros: Ação e aventura. Classificação: Livre',
  1
);

INSERT INTO Produtos(id, nome, fabricante, modelo, preco, descricao, especificacoes, ativo)
VALUES (
  22,
  'The Legend of Zelda: Echoes of Wisdom',
  'Nintendo',
  null,
  299.99,
  'Salve Hyrule, desta vez, com a sabedoria da princesa Zelda! O povo de Hyrule está sendo engolido por estranhas fendas que surgiram, com um certo espadachim e o rei de Hyrule e seus conselheiros entre os desaparecidos. Sozinha, agora cabe à princesa Zelda salvar seu reino na última aventura da série The Legend of Zelda™!',
  'Plataformas: Nintendo Switch. Gêneros: Ação e aventura. Classificação: Livre',
  1
);

INSERT INTO Produtos(id, nome, fabricante, modelo, preco, descricao, especificacoes, ativo)
VALUES (
  23,
  'Shadow of the Tomb Raider',
  'Nintendo',
  null,
  159.99,
  'Vivencie o momento definitivo de Lara Croft em Tomb Raider. Em Shadow of the Tomb Raider, Lara precisa dominar uma selva letal, superar tumbas assustadoras e perseverar em seu momento mais difícil. Enquanto ela corre contra o tempo para salvar o mundo do apocalipse maia, Lara precisa se tornar a desbravadora que está destinada a ser',
  'Plataformas: PlayStation 4, Xbox One, PC. Gêneros: Aventura. Classificação: 16 anos',
  1
);

INSERT INTO Produtos(id, nome, fabricante, modelo, preco, descricao, especificacoes, ativo)
VALUES (
  24,
  'Silent Hill 2 Remake',
  'Konami',
  null,
  349.99,
  'Assuma o papel de James Sunderland e explore a quase deserta cidade de Silent Hill neste muito aguardado remake do clássico de 2001. Atraído até este lugar misterioso por uma carta de sua esposa, que morreu há três anos, James vasculha a cidade atrás de vestígios dela',
  'Plataformas: PlayStation 5, PC. Gêneros: Survival horror. Classificação: 18 anos',
  1
);

INSERT INTO Produtos(id, nome, fabricante, modelo, preco, descricao, especificacoes, ativo)
VALUES (
  25,
  'Metal Gear Solid V: The Phantom Pain',
  'Konami',
  null,
  89.99,
  'Se passando nove anos após os acontecimentos de MGSV: Ground Zeroes e a queda da Mother Base, Snake, também chamado de Big Boss, acorda de um coma nove anos depois. O jogo recomeça a história em 1984, com a Guerra Fria ainda como pano de fundo, continuando a dar forma a uma crise global. A jornada de Snake o leva a um mundo onde ele é impulsionado por uma necessidade de vingança e a perseguição de um grupo de criminosos, XOF',
  'Plataformas: PlayStation 4, PlayStation 3, Xbox One, Xbox 360, PC. Gêneros: Ação e mundo aberto. Classificação: 18 anos',
  1
);

INSERT INTO Produtos(id, nome, fabricante, modelo, preco, descricao, especificacoes, ativo)
VALUES (
  26,
  'Astro Bot',
  'Sony',
  null,
  299.99,
  'A nave-mãe PS5® foi destruída, deixando ASTRO e sua tripulação de bots espalhada pelas galáxias. Hora de embarcar na sua fiel Dual Speeder e conhecer mais de 50 planetas cheios de diversão, perigos e surpresas. Em sua jornada, aproveite ao máximo os novos poderes de ASTRO e reencontre várias lendas do universo PlayStation',
  'Plataformas PlayStation 5, Android. Gêneros: Ação. Classificação: Livre',
  1
);

INSERT INTO Produtos(id, nome, fabricante, modelo, preco, descricao, especificacoes, ativo)
VALUES (
  27,
  'Mortal Kombat 1',
  'Warner Bros. Games',
  null,
  249.99,
  'Descubra um Universo renascido de Mortal Kombat™ criado pelo Deus do Fogo Liu Kang. Mortal Kombat™ 1 inaugura uma nova era da franquia icônica com um novo sistema de luta, modos de jogo e fatalities!',
  'Plataformas PlayStation 5, Android. Gêneros: Ação. Classificação: Livre',
  1
);

INSERT INTO Produtos(id, nome, fabricante, modelo, preco, descricao, especificacoes, ativo)
VALUES (
  28,
  'Elden Ring',
  'FromSoftware',
  null,
  299.99,
  'Nas Terras Intermediárias governadas pela Rainha Marika, a Eterna, o Anel Elden, a fonte da Erdtree, foi destruído. Os descendentes de Marika, todos semideuses, reivindicaram os fragmentos do Anel Elden conhecidos como as Grandes Runas, e a mancha louca de sua força recém-descoberta desencadeou uma guerra: A Destruição. Uma guerra que significou o abandono pela Vontade Maior',
  'Plataformas: PlayStation 5, Nintendo Switch, Xbox Series X e Series S, PC. Gêneros: RPG. Classificação: 16 anos',
  1
);
