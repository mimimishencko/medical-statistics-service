import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {InformPageComponent} from './inform-page/inform-page.component';
import {ChooseCritetiumComponent} from './choose-critetium/choose-critetium.component';
import {InteractiveHelperComponent} from './interactive-helper/interactive-helper.component';
import {ManualUploadComponent} from './manual-upload/manual-upload.component';


const routes: Routes = [
  {
    path: '',
    pathMatch: 'full',
    component: InformPageComponent,
    data: {title: 'Inform'},
  },
  {
    path: 'choose-criterion',
    component: ChooseCritetiumComponent,
    data: {title: 'Criterion'}
  },
  {
    path: 'interactive-helper',
    component: InteractiveHelperComponent,
    data: {title: 'Helper'},
  },
  {
    path: 'manual-input',
    component: ManualUploadComponent,
    data: {title: 'Manual Input'},
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
