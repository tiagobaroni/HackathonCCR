﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace bmo.views
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class selecaModo : ContentPage
    {
        public selecaModo()
        {
            InitializeComponent();
        }
        private void GoMenu(object sender, EventArgs args)
        {
            Navigation.PushAsync(new views.menu());
        }
    }
}