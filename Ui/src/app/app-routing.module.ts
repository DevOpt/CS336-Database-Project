import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { WelcomeComponent } from './welcome/welcome.component';
import { BarDetailsComponent } from  './bar-details/bar-details.component';
import { BeerDetailsComponent } from './beer-details/beer-details.component';
import { BeersComponent } from './beers/beers.component';
import { ManufacturersComponent } from './manufacturers/manufacturers.component'
import { ManufacturerDetailsComponent } from './manufacturer-details/manufacturer-details.component';
import { DrinkersComponent } from './drinkers/drinkers.component';
import { DrinkerDetailsComponent } from './drinker-details/drinker-details.component';

const routes: Routes = [
  {
    path: '',
    pathMatch: 'full',
    redirectTo: 'bars'
  },
  {
    path: 'bars',
    pathMatch: 'full',
    component: WelcomeComponent
  },
  {
    path: 'bars/:bar',
    pathMatch: 'full',
    component: BarDetailsComponent
  },
  {
    path: 'beers',
    pathMatch: 'full',
    component: BeersComponent
  },
  {
    path: 'beers/:beer',
    pathMatch: 'full',
    component: BeerDetailsComponent
  },
  {
    path: 'manufacturers',
    pathMatch: 'full',
    component: ManufacturersComponent
  },
  {
    path: 'manufacturers/:manf',
    pathMatch: 'full',
    component: ManufacturerDetailsComponent
  },
  {
    path: 'drinkers',
    pathMatch: 'full',
    component: DrinkersComponent
  },
  {
    path: 'drinkers/:drinker',
    pathMatch: 'full',
    component: DrinkerDetailsComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
