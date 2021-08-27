const convert = require('convert-units')

module.exports = {
    Convert(input, out, string) {
        //Conversion Function
        let finalMessage = "";
        if(string.toLowerCase().includes(input)) {
            let i = 0;
            let x;
            let s = 0;
            let TempMessage = string.toLowerCase();
            while(i >= 0) {
                x = ""
                i = TempMessage.indexOf(input, s);
                s = i + 1;
                i--;
                while(TempMessage[i] == ' ') 
                    i--;
                while(i >= 0 && TempMessage[i] != ' ' && !isNaN(TempMessage[i])) {
                    x += TempMessage[i];
                    i--;
                }
                x = x.split("").reverse().join("");
                if(x.length > 0 && !isNaN(x)) {
                    finalMessage += x + input + " = " + convert(parseInt(x)).from(input).to(out).toFixed(0) + out + "\n";
                }
            }
        }
        return finalMessage;
    },
    ConvertInput(string){
        let finalMessage = "";
        //LB to KG
        finalMessage += this.Convert('lb', 'kg', string);
        finalMessage += this.Convert('kg', 'lb', string);

        return finalMessage;
    }
};
