import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { InformPageComponent } from './inform-page/inform-page.component';
import { InteractiveHelperComponent } from './interactive-helper/interactive-helper.component';
import { ManualUploadComponent } from './manual-upload/manual-upload.component';
import { ChooseCritetiumComponent } from './choose-critetium/choose-critetium.component';
import {HttpClientModule} from '@angular/common/http';
import {ReactiveFormsModule} from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    InformPageComponent,
    InteractiveHelperComponent,
    ManualUploadComponent,
    ChooseCritetiumComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
