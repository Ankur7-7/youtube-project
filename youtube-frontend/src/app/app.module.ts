import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import {MatTabsModule} from "@angular/material/tabs";
import {MatInputModule} from "@angular/material/input";
import {MatButtonModule} from "@angular/material/button";
import {FormsModule} from "@angular/forms";
import {MatFormFieldModule} from "@angular/material/form-field";
import { YouTubePlayerModule } from '@angular/youtube-player';
import {MatCardModule} from "@angular/material/card";
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { VideoCommentsComponent } from './video-comments/video-comments.component';
import { CommentsService } from './service/comments.service';
import { HttpClientModule } from '@angular/common/http';
import { CommentsComponent } from './comments/comments.component';
import {MatPaginatorModule} from '@angular/material/paginator';
import {MatTableModule} from '@angular/material/table';
import {ScrollingModule} from '@angular/cdk/scrolling';
import {MatListModule} from '@angular/material/list';
import {MatButtonToggleModule} from '@angular/material/button-toggle';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    VideoCommentsComponent,
    CommentsComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MatTabsModule,
    FormsModule,
    MatButtonModule,
    MatFormFieldModule,
    MatInputModule,
    YouTubePlayerModule,
    MatCardModule,
    MatPaginatorModule,
    BrowserAnimationsModule,
    HttpClientModule,
    MatTableModule,
    ScrollingModule,
    MatListModule,
    MatButtonToggleModule
  ],
  providers: [CommentsService],
  bootstrap: [AppComponent]
})
export class AppModule { }
