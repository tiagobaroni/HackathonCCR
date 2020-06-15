using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Xamarin.Forms;

namespace bmo
{
    // Learn more about making custom code visible in the Xamarin.Forms previewer
    // by visiting https://aka.ms/xamarinforms-previewer
    [DesignTimeVisible(false)]
    public partial class MainPage : ContentPage
    {
        public MainPage()
        {
            InitializeComponent();
        }

        private void GoEntrar(object sender, EventArgs args)
        {
            Navigation.PushAsync(new views.entrar());
            var page = new views.entrar();

            Navigation.PushAsync(page);
        }

        private void GoCadastroMail(object sender, EventArgs args)
        {
            Navigation.PushAsync(new views.cadastroMail());
            var page = new views.cadastroMail();

            Navigation.PushAsync(page);
        }

        private void ShowMesageFacebook(object sender, EventArgs args)
        {
            DisplayAlert("Atenção", "Cadastro usando API do Facebook não implementado - API Key não liberada pelo Facebook!", "OK");
        }

        private void ShowMesageGoogle(object sender, EventArgs args)
        {
            DisplayAlert("Atenção", "Cadastro usando API do Google não implementado!", "OK");
        }
    }
}
