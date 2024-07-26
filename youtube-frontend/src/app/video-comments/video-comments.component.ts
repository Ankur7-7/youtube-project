import { Component, OnInit, ViewChild } from '@angular/core';
import { CommentsService } from '../service/comments.service';
import { Comment } from '../comment.interface';
import {PageEvent} from "@angular/material/paginator";

@Component({
  selector: 'app-video-comments',
  templateUrl: './video-comments.component.html',
  styleUrls: ['./video-comments.component.scss']
})
export class VideoCommentsComponent{

  search!: string;
  video_list : any[]=[
    {
      "etag": "1IDu9lx29lE-BeXU4vkHZA6ldN4",
      "id": {
        "kind": "youtube#video",
        "videoId": "gHnWkmW6qRI"
      },
      "kind": "youtube#searchResult",
      "snippet": {
        "channelId": "UCfCv0ckR89HTy2ASEgZHNSg",
        "channelTitle": "Happy Bachpan",
        "description": "A For Apple B For Ball C For Cat D For Dog Nursery Rhyme by Shaan is a preschool/kindergarten song that will help kids and ...",
        "liveBroadcastContent": "none",
        "publishTime": "2023-07-29T01:45:01Z",
        "publishedAt": "2023-07-29T01:45:01Z",
        "thumbnails": {
          "default": {
            "height": 90,
            "url": "https://i.ytimg.com/vi/gHnWkmW6qRI/default.jpg",
            "width": 120
          },
          "high": {
            "height": 360,
            "url": "https://i.ytimg.com/vi/gHnWkmW6qRI/hqdefault.jpg",
            "width": 480
          },
          "medium": {
            "height": 180,
            "url": "https://i.ytimg.com/vi/gHnWkmW6qRI/mqdefault.jpg",
            "width": 320
          }
        },
        "title": "A For Apple B For Ball I Abcd Song I Abcd Rhymes I Abc Song Nursery Rhymes I Happy Bachpan"
      }
    },
    {
      "etag": "DJqKju4ImVW8ErhZDYvisfuvofc",
      "id": {
        "kind": "youtube#video",
        "videoId": "4aaAAJ-acBo"
      },
      "kind": "youtube#searchResult",
      "snippet": {
        "channelId": "UCaUPL4N_oalhAS_sQHJXOEg",
        "channelTitle": "Blanki Kids World - \u0939\u093f\u0902\u0926\u0940",
        "description": "Learn the Alphabet in Hindi | Learn ABCD in Hindi & English | Learn ABC Letters In this educational video, kids can learn all the ...",
        "liveBroadcastContent": "none",
        "publishTime": "2023-05-25T12:00:05Z",
        "publishedAt": "2023-05-25T12:00:05Z",
        "thumbnails": {
          "default": {
            "height": 90,
            "url": "https://i.ytimg.com/vi/4aaAAJ-acBo/default.jpg",
            "width": 120
          },
          "high": {
            "height": 360,
            "url": "https://i.ytimg.com/vi/4aaAAJ-acBo/hqdefault.jpg",
            "width": 480
          },
          "medium": {
            "height": 180,
            "url": "https://i.ytimg.com/vi/4aaAAJ-acBo/mqdefault.jpg",
            "width": 320
          }
        },
        "title": "Learn the Alphabet in Hindi | Learn ABCD in Hindi &amp; English | Learn ABC Letters"
      }
    },
    {
      "etag": "CZIUFi_DHyTlofQvU1njcl3pRpk",
      "id": {
        "kind": "youtube#video",
        "videoId": "hq3yfQnllfQ"
      },
      "kind": "youtube#searchResult",
      "snippet": {
        "channelId": "UCBnZ16ahKA2DZ_T5W0FPUXg",
        "channelTitle": "ChuChu TV Nursery Rhymes & Kids Songs",
        "description": "You can listen to this song on Spotify - https://chuchu.me/PhonicsSong To download and watch this video anywhere and at any ...",
        "liveBroadcastContent": "none",
        "publishTime": "2014-03-06T20:57:50Z",
        "publishedAt": "2014-03-06T20:57:50Z",
        "thumbnails": {
          "default": {
            "height": 90,
            "url": "https://i.ytimg.com/vi/hq3yfQnllfQ/default.jpg",
            "width": 120
          },
          "high": {
            "height": 360,
            "url": "https://i.ytimg.com/vi/hq3yfQnllfQ/hqdefault.jpg",
            "width": 480
          },
          "medium": {
            "height": 180,
            "url": "https://i.ytimg.com/vi/hq3yfQnllfQ/mqdefault.jpg",
            "width": 320
          }
        },
        "title": "Phonics Song with TWO Words - A For Apple - ABC Alphabet Songs with Sounds for Children"
      }
    },
    {
      "etag": "I7br2_RuQlxqQ8cu4t7TZ-1HvOE",
      "id": {
        "kind": "youtube#video",
        "videoId": "8fLfkK2kPcs"
      },
      "kind": "youtube#searchResult",
      "snippet": {
        "channelId": "UCc0cGIbYYj79_IUI2A70UjQ",
        "channelTitle": "Beep Beep - Nursery Rhymes",
        "description": "Emma and Joey are playing with cute little duckies. When they count the duckies, they foundout some duckies are missing.",
        "liveBroadcastContent": "none",
        "publishTime": "2023-06-22T11:45:11Z",
        "publishedAt": "2023-06-22T11:45:11Z",
        "thumbnails": {
          "default": {
            "height": 90,
            "url": "https://i.ytimg.com/vi/8fLfkK2kPcs/default.jpg",
            "width": 120
          },
          "high": {
            "height": 360,
            "url": "https://i.ytimg.com/vi/8fLfkK2kPcs/hqdefault.jpg",
            "width": 480
          },
          "medium": {
            "height": 180,
            "url": "https://i.ytimg.com/vi/8fLfkK2kPcs/mqdefault.jpg",
            "width": 320
          }
        },
        "title": "Number Song | Five Little Duckies + More Baby Songs | Beep Beep Nursery Rhymes"
      }
    },
    {
      "etag": "EavYw-L6V1N45J8xQIgC2oi-Zew",
      "id": {
        "kind": "youtube#video",
        "videoId": "dx2_0pVvV2U"
      },
      "kind": "youtube#searchResult",
      "snippet": {
        "channelId": "UCJplp5SjeGSdVdwsfb9Q7lQ",
        "channelTitle": "Like Nastya",
        "description": "Funny kids song about alphabet and other kids music videos Subscribe to Like Nastya - https://is.gd/gdv8uX Instagram ...",
        "liveBroadcastContent": "none",
        "publishTime": "2023-06-23T08:00:28Z",
        "publishedAt": "2023-06-23T08:00:28Z",
        "thumbnails": {
          "default": {
            "height": 90,
            "url": "https://i.ytimg.com/vi/dx2_0pVvV2U/default.jpg",
            "width": 120
          },
          "high": {
            "height": 360,
            "url": "https://i.ytimg.com/vi/dx2_0pVvV2U/hqdefault.jpg",
            "width": 480
          },
          "medium": {
            "height": 180,
            "url": "https://i.ytimg.com/vi/dx2_0pVvV2U/mqdefault.jpg",
            "width": 320
          }
        },
        "title": "Nastya ABC Song and more Music Videos for kids"
      }
    },
    {
      "etag": "qz4IDxb6sWyzZC2mTYd6yEI0YM4",
      "id": {
        "kind": "youtube#video",
        "videoId": "OuskxtK0C6s"
      },
      "kind": "youtube#searchResult",
      "snippet": {
        "channelId": "UCrZ5za3HHU3Aj1BvoeCVOhw",
        "channelTitle": "Funnywe\ud83d\ude43",
        "description": "A for apple | \u0905 \u0938\u0947 \u0905\u0928\u093e\u0930 | abcd | phonics song | a for apple b for ball c for cat | abcd song | abcde #abcd #nurseryrhymes #art ...",
        "liveBroadcastContent": "none",
        "publishTime": "2023-07-12T00:30:10Z",
        "publishedAt": "2023-07-12T00:30:10Z",
        "thumbnails": {
          "default": {
            "height": 90,
            "url": "https://i.ytimg.com/vi/OuskxtK0C6s/default.jpg",
            "width": 120
          },
          "high": {
            "height": 360,
            "url": "https://i.ytimg.com/vi/OuskxtK0C6s/hqdefault.jpg",
            "width": 480
          },
          "medium": {
            "height": 180,
            "url": "https://i.ytimg.com/vi/OuskxtK0C6s/mqdefault.jpg",
            "width": 320
          }
        },
        "title": "A for apple | \u0905 \u0938\u0947 \u0905\u0928\u093e\u0930 | abcd | phonics song | a for apple b for ball c for cat | abcd song | abcde"
      }
    },
    {
      "etag": "6GLzI3eF0IzmNLVC1ds7038zWH4",
      "id": {
        "kind": "youtube#video",
        "videoId": "aLXONLMWe44"
      },
      "kind": "youtube#searchResult",
      "snippet": {
        "channelId": "UCJm7UPWbVhuNe3achnRi8iA",
        "channelTitle": "Eden Mu\u00f1oz",
        "description": "Eden Mu\u00f1oz & Junior H\u2013 Abcdario (Video Oficial) Familia ya est\u00e1 disponible mi nuevo Sencillo: https://EdenM.lnk.to/Abecedario ...",
        "liveBroadcastContent": "none",
        "publishTime": "2023-05-15T22:00:10Z",
        "publishedAt": "2023-05-15T22:00:10Z",
        "thumbnails": {
          "default": {
            "height": 90,
            "url": "https://i.ytimg.com/vi/aLXONLMWe44/default.jpg",
            "width": 120
          },
          "high": {
            "height": 360,
            "url": "https://i.ytimg.com/vi/aLXONLMWe44/hqdefault.jpg",
            "width": 480
          },
          "medium": {
            "height": 180,
            "url": "https://i.ytimg.com/vi/aLXONLMWe44/mqdefault.jpg",
            "width": 320
          }
        },
        "title": "Eden Mu\u00f1oz &amp; Junior H\u2013 Abcdario (Video Oficial)"
      }
    },
    {
      "etag": "JhdVnQtts8l9NNn7msGS0IWwCAE",
      "id": {
        "kind": "youtube#video",
        "videoId": "NvdUSZyCGRs"
      },
      "kind": "youtube#searchResult",
      "snippet": {
        "channelId": "UCx790OVgpTC1UVBQIqu3gnQ",
        "channelTitle": "\u2605 Kids Roma Show",
        "description": "Roma and Diana learn the English Alphabet. ABC song for kids Roma's Instagram: https://www.instagram.com/kidsromashow/ ...",
        "liveBroadcastContent": "none",
        "publishTime": "2021-04-27T10:15:02Z",
        "publishedAt": "2021-04-27T10:15:02Z",
        "thumbnails": {
          "default": {
            "height": 90,
            "url": "https://i.ytimg.com/vi/NvdUSZyCGRs/default.jpg",
            "width": 120
          },
          "high": {
            "height": 360,
            "url": "https://i.ytimg.com/vi/NvdUSZyCGRs/hqdefault.jpg",
            "width": 480
          },
          "medium": {
            "height": 180,
            "url": "https://i.ytimg.com/vi/NvdUSZyCGRs/mqdefault.jpg",
            "width": 320
          }
        },
        "title": "Roma and Diana learn the alphabet / ABC song"
      }
    }];
  video_id: string="";
  video!: any;
  comments!: Comment[];
  funnyCom !:any[];
  positiveCom !:any[];
  summary !: string;
  sentiments!: string[];
  playerWidth !: any;
  playerHeight !: any;
  screenWidth: any;  
  screenHeight: any;  

  i =0; 
  length =50;
  pageSize = 5;
  pageIndex = 0;
  pageSizeOptions = [5, 10, 25];

  hidePageSize = true;
  showPageSizeOptions = true;
  showFirstLastButtons = true;
  disabled = false;

  pageEvent!: PageEvent;
  loader : string = "assets/loaders/loading.gif";
  IsPlayer: boolean = false;
  IsList: boolean = false;
  IsComments : boolean = false;
  IsLoader : boolean = false;
  topCom!: any[];


  handlePageEvent(e: PageEvent) {
    this.pageEvent = e;
    this.length = e.length;
    this.pageSize = e.pageSize;
    this.pageIndex = e.pageIndex;
  } 

  ngOnInit() {  

    this.screenWidth = window.innerWidth;
    this.screenHeight = window.innerHeight;  

    if(this.screenWidth >= 800)
      this.playerWidth = 0.45*this.screenWidth;
    else
      this.playerWidth = 0.9*this.screenWidth;

    this.playerHeight = 0.6*this.playerWidth;
}  

  constructor(private commentsService: CommentsService) {}

  // ngOnInit(): void {
  //   if(this.search)
  //     this.commentsService.fetch_comments(this.search).subscribe(result => {
  //       this.comments=result["comments"];
  //       this.video_list = result["videos"];
  //       this.video_id = this.video_list[0]["id"]["videoId"]
  //     })
  // }

  fetch_data(): void{
    if(this.search)
      this.commentsService.fetch_comments(this.search).subscribe(result => {
        this.comments=result["comments"];
        this.topCom = result["comments"];
        this.funnyCom=result["funny_com"];
        this.positiveCom=result["positive_com"];
        this.video_list = result["videos"].slice(0, 10);
        // this.video = this.video_list[0];
        this.sentiments = result["sentiments"];
        this.summary = result["summary"];

        this.IsLoader = false;

        // while(!this.video["id"]["videoId"]){
        //   this.i = this.i+1;
        //   this.video = this.video_list[this.i];
        // }

        // this.video_id = this.video["id"]["videoId"];
        if(this.comments){
          this.IsComments = true;
          console.log("comments retrieved");
        }
        if(this.video_list)
          this.IsList = true;
      })
  }


  OnSubmit(event:Event){
    this.fetch_data();
    console.log("Submit Button Works" + this.search);
    if(this.comments) console.log("comments retrieved");
    this.IsPlayer = false;
    this.IsList = false;
    this.IsComments = false;
    this.IsLoader = true;
  }

  OnClick(videoId:string){
    this.video_id = videoId;
    this.IsPlayer = true;
    this.IsList = false;
    console.log(videoId);
  }

  ChangeFilter(filter: string){
    
    console.log("Comments Filter: " + filter);

    if(filter=="top")
      this.comments = this.topCom;
    else if(filter=="funny")
      this.comments=this.funnyCom;
    else if(filter=="positive")
      this.comments = this.positiveCom;

  }
}
