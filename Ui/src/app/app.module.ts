import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule, HttpClient } from '@angular/common/http';
import { TableModule, Table } from 'primeng/table';
import { DropdownModule } from 'primeng/dropdown'
import { BrowserAnimationsModule } from '@angular/platform-browser/animations'
import { FormsModule } from '@angular/forms'
 
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { WelcomeComponent } from './welcome/welcome.component';
import { BarDetailsComponent } from './bar-details/bar-details.component';
import { BeerDetailsComponent } from './beer-details/beer-details.component';
import { BeersComponent } from './beers/beers.component';
import { ManufacturersComponent } from './manufacturers/manufacturers.component';
import { ManufacturerDetailsComponent } from './manufacturer-details/manufacturer-details.component';
import { DrinkersComponent } from './drinkers/drinkers.component';
import { DrinkerDetailsComponent } from './drinker-details/drinker-details.component';


@NgModule({
  declarations: [
    AppComponent,
    WelcomeComponent,
    BarDetailsComponent,
    BeerDetailsComponent,
    BeersComponent,
    ManufacturersComponent,
    ManufacturerDetailsComponent,
    DrinkersComponent,
    DrinkerDetailsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    DropdownModule,
    TableModule,
    FormsModule,
    BrowserAnimationsModule
  ],
  providers: [HttpClient],
  bootstrap: [AppComponent]
})
export class AppModule { }
