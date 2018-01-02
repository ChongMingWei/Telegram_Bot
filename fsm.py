from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

        
    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'a'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'b'

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'c'
		
    def on_enter_state1(self, update):
        update.message.reply_text("資訊所的教授有:高宏宇、連震杰、李同益、吳宗憲、孫永年、黃崇明、謝孫源、黃宗立、郭耀煌、蔣榮先、陳培殷、李強、鄭憲宗、蘇文鈺、張燕光、郭淑美、王士豪、蘇銓清、蕭宏章、張大緯、梁勝富、許靜芳、盧文祥、楊中平、藍崑展、林英超、吳明龍、趙梓程、蔡孟勳、李信杰、莊坤達、胡敏君、涂嘉恒、張瑞紘")
        self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text("醫資所的教授有:高宏宇、孫永年、謝孫源、郭耀煌、蔣榮先、蘇文鈺、張燕光、郭淑美、王士豪、蘇銓清、蕭宏章、梁勝富、盧文祥、楊中平、藍崑展、吳明龍、趙梓程、莊坤達")
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')
		
    def on_enter_state3(self, update):
        update.message.reply_text("製造所的教授有:連震杰、鄭芳田、陳裕民、陳響亮、楊大和、陳朝鈞、李家岩、蔡佩璇")
        self.go_back(update)

    def on_exit_state3(self, update):
        print('Leaving state3')
