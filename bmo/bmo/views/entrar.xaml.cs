using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace bmo.views
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class entrar : ContentPage
    {
        public entrar()
        {
            InitializeComponent();
        }

        private void GoSelecaoModo(object sender, EventArgs args)
        {
            Navigation.PushAsync(new views.selecaModo());
            var page = new views.selecaModo();

            Navigation.PushAsync(page);
            //NavigationPage.SetHasNavigationBar(page, false);

        }
    }
}